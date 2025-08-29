import os
from dotenv import load_dotenv
from app.db.movies_catalog import Neo4jMoviesCatalog


def main():
    try:
        load_dotenv()

        neo4j_uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        neo4j_user = os.getenv("NEO4J_USER", "neo4j")
        neo4j_password = os.getenv("NEO4J_PASSWORD", "")
        neo4j_db_name = os.getenv("NEO4J_DB_NAME", "movies")
        movies_csv_path = os.getenv("MOVIES_DATASET_CSV_PATH", "data/tmdb_5000_movies.csv")
        credits_csv_path = os.getenv("CREDITS_DATASET_CSV_PATH", "data/tmdb_5000_credits.csv")

        print("Setting up catalog...")

        with Neo4jMoviesCatalog(neo4j_uri,  neo4j_user, neo4j_password, neo4j_db_name) as catalog:
            #TODO: Remove after testing
            catalog.query("MATCH (n) DETACH DELETE n;")

            # If catalog is empty, populate it with movies from CSV dataset
            if catalog.is_empty():
                print(f"Populating catalog with movies from CSV file: {movies_csv_path} ...")
                movies_count = catalog.populate_movies_from_csv(movies_csv_path, limit=100, chunk_size=10)
                print(f"Catalog populated with {movies_count} movies.")

                print(f"Populating catalog with credits from CSV file: {credits_csv_path} ...")
                credits_count = catalog.populate_credits_from_csv(credits_csv_path, limit=100, chunk_size=10)
                print(f"Catalog populated with {credits_count} credits.")

            print("Catalog setup complete.\n")

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
