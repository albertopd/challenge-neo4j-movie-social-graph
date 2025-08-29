import math
import pandas as pd
from neo4j import GraphDatabase
from app.pipelines.transform_credits import transform_credits
from app.pipelines.transform_movies import transform_movies


class Neo4jMoviesCatalog:
    def __init__(self, uri: str, user: str, password: str, db_name: str):
        if not uri or uri.strip() == "":
            raise ValueError("The 'uri' parameter must be a non-empty string.")
        if not user or user.strip() == "":
            raise ValueError("The 'user' parameter must be a non-empty string.")
        if not password or password.strip() == "":
            raise ValueError("The 'password' parameter must be a non-empty string.")
        if not db_name or db_name.strip() == "":
            raise ValueError("The 'db_name' parameter must be a non-empty string.") 

        self.__driver = GraphDatabase.driver(uri, auth=(user, password))
        self.__driver.verify_connectivity()
        self.__db_name = db_name

    def close(self):
        if self.__driver is not None:
            self.__driver.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def _get_total_chunks(
        self, 
        csv_path: str, 
        chunksize: int
    ) -> int:
        """
        Calculates the total number of chunks required to process a CSV file in batches.

        Args:
            csv_path (str): The file path to the CSV file.
            chunksize (int): The number of rows per chunk.

        Returns:
            int: The total number of chunks needed to process the file. Returns 0 if an error occurs.

        Notes:
            Assumes the first row of the CSV file is a header and excludes it from the row count.
        """
        try:
            with open(csv_path, "rb") as f:
                total_rows = sum(1 for _ in f) - 1  # subtract header row
            return math.ceil(total_rows / chunksize)
        except Exception as e:
            print(f"Error occurred while getting total chunks: {e}")
            return 0
        
    def is_empty(self) -> bool:
        query = "MATCH (n) RETURN count(n) as total"
        result = self.query(query)
        return result[0]['total'] == 0 if result else True

    def populate_movies_from_csv(
        self,
        csv_path: str,
        limit: int | None = None,
        chunk_size: int = 5000,
    ) -> int:
        total_chunks = self._get_total_chunks(csv_path, chunk_size)
        total_processed = 0
        total_inserted = 0

        reader = pd.read_csv(csv_path, chunksize=chunk_size)

        for i, chunk in enumerate(reader):
            print(f"Processing chunk {i + 1} out of {total_chunks} : {chunk.shape[0]} rows")

            # Respect the limit if provided
            if limit is not None:
                remaining = limit - total_processed
                if remaining <= 0:
                    break
                chunk = chunk.head(remaining)

            # Apply transformation pipeline
            chunk = transform_movies(chunk)

            # Insert into Neo4j
            movies = chunk.to_dict(orient="records")
            if movies:
                result = self.add_movies(movies)
                total_inserted += result[0]['total']

            total_processed += chunk.shape[0]

        return total_inserted
    
    def populate_credits_from_csv(
        self,
        csv_path: str,
        limit: int | None = None,
        chunk_size: int = 5000,
    ) -> int:
        total_chunks = self._get_total_chunks(csv_path, chunk_size)
        total_processed = 0
        total_inserted = 0

        reader = pd.read_csv(csv_path, chunksize=chunk_size)

        for i, chunk in enumerate(reader):
            print(f"Processing chunk {i + 1} out of {total_chunks} : {chunk.shape[0]} rows")

            # Respect the limit if provided
            if limit is not None:
                remaining = limit - total_processed
                if remaining <= 0:
                    break
                chunk = chunk.head(remaining)

            # Apply transformation pipeline
            chunk = transform_credits(chunk)

            # Insert into Neo4j
            credits = chunk.to_dict(orient="records")
            if credits:
                result = self.add_credits(credits)
                total_inserted += result[0]['total']

            total_processed += chunk.shape[0]

        return total_inserted

    def query(self, query, parameters = None):
        with (self.__driver.session(database =self.__db_name)) as session:
            return list(session.run(query, parameters))
    
    def add_movies(self, rows):
        query = """
            UNWIND $rows AS row
            MERGE (m:Movie {movie_id: row.id})
              ON CREATE SET m.title = row.title,
                            m.original_title = row.original_title,
                            m.release_date = row.release_date,
                            m.status = row.status,
                            m.runtime = row.runtime,
                            m.budget = row.budget,
                            m.revenue = row.revenue,
                            m.homepage = row.homepage,
                            m.tagline = row.tagline,
                            m.overview = row.overview,
                            m.popularity = row.popularity,
                            m.vote_average = row.vote_average,
                            m.vote_count = row.vote_count
        """
        query += self._merge_genres()
        query += self._merge_keywords()
        query += self._merge_companies()
        query += self._merge_countries()
        query += self._merge_languages()
        query += "RETURN count(*) as total"

        return self.query(query, parameters={'rows': rows})

    def _merge_genres(self):
        return """
            FOREACH (g IN row.genres |
              MERGE (genre:Genre {name: g.name})
              MERGE (m)-[:HAS_GENRE]->(genre)
            )
        """

    def _merge_keywords(self):
        return """
            FOREACH (k IN row.keywords |
              MERGE (keyword:Keyword {name: k.name})
              MERGE (m)-[:HAS_KEYWORD]->(keyword)
            )
        """

    def _merge_companies(self):
        return """
            FOREACH (c IN row.production_companies |
              MERGE (pc:ProductionCompany {name: c.name})
              MERGE (m)-[:PRODUCED_BY]->(pc)
            )
        """

    def _merge_countries(self):
        return """
            FOREACH (pc IN row.production_countries |
              MERGE (c:Country {iso_code: pc.iso_3166_1, name: pc.name})
              MERGE (m)-[:PRODUCED_IN]->(c)
            )
        """

    def _merge_languages(self):
        return """
            FOREACH (sl IN row.spoken_languages |
              MERGE (l:Language {iso_code: sl.iso_639_1, name: sl.name})
              MERGE (m)-[:HAS_LANGUAGE]->(l)
            )
        """
    
    def add_credits(self, rows):
        query = """
            UNWIND $rows AS row
            MATCH (m:Movie {movie_id: row.movie_id})
        """
        query += self._merge_cast()
        query += self._merge_crew()
        query += "RETURN count(*) as total"

        return self.query(query, parameters={'rows': rows})

    def _merge_cast(self):
        return """
            FOREACH (c IN row.cast |
                MERGE (pc:Person {person_id: c.id})
                ON CREATE SET pc.name = c.name, 
                            pc.gender = c.gender
                MERGE (pc)-[r:ACTED_IN]->(m)
                SET r.character = c.character
            )
        """
    
    def _merge_crew(self):
        return """
            FOREACH (cr IN row.crew |
                MERGE (pr:Person {person_id: cr.id})
                ON CREATE SET pr.name = cr.name, 
                            pr.gender = cr.gender
                FOREACH (_ IN CASE WHEN toLower(cr.job) = 'director' THEN [1] ELSE [] END |
                    MERGE (pr)-[:DIRECTED]->(m)
                )
                FOREACH (_ IN CASE WHEN toLower(cr.job) <> 'director' THEN [1] ELSE [] END |
                    MERGE (pr)-[r:CONTRIBUTED_TO]->(m)
                    SET r.job = cr.job,
                        r.department = cr.department,
                        r.credit_id = cr.credit_id
                )
            )
        """
