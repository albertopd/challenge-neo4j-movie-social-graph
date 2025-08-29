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
            # If catalog is empty, populate it with movies from CSV dataset
            if catalog.is_empty():
                print(f"Populating catalog with movies from CSV file: {movies_csv_path} ...")
                movies_count = catalog.populate_movies_from_csv(movies_csv_path, limit=100, chunk_size=10)
                print(f"Catalog populated with {movies_count} movies.")

                print(f"Populating catalog with credits from CSV file: {credits_csv_path} ...")
                credits_count = catalog.populate_credits_from_csv(credits_csv_path, limit=100, chunk_size=10)
                print(f"Catalog populated with {credits_count} credits.")

            print("Catalog setup complete.\n")

            # Find movies by a specific director
            director_name = "Christopher Nolan"
            movies = catalog.find_movies_by_director(director_name)
            if movies:
                print(f"Movies directed by {director_name}:")
                for movie in movies:
                    print(f" - \"{movie['title']}\" ({movie['release_date'].year})")
            else:
                print(f"No movies found for director: {director_name}")

            # Find movies by specific actors
            actor_names = ["Chris Evans", "Chris Hemsworth"]
            movies = catalog.find_movies_by_actors(actor_names)
            if movies:
                print(f"\nMovies featuring {', '.join(actor_names)}:")
                for movie in movies:
                    print(f" - \"{movie['title']}\" ({movie['release_date'].year})")
            else:
                print(f"\nNo movies found for actors: {', '.join(actor_names)}")

            # Find movies by a specific genre afte certain year
            genre_name = "Fantasy"
            after_year = 2010
            movies = catalog.find_movies_by_genre(genre_name, after_year)
            if movies:
                print(f"\nMovies in the {genre_name} genre (after {after_year}):")
                for movie in movies:
                    print(f" - \"{movie['title']}\" ({movie['release_date'].year})")
            else:
                print(f"\nNo movies found in the {genre_name} genre (after {after_year}).")

            # Find movies produced in Canada
            country_code = "CA"
            movies = catalog.find_movies_produced_in_country(country_code)
            if movies:
                print(f"\nMovies produced in {country_code}:")
                for movie in movies:
                    print(f" - \"{movie['title']}\" ({movie['release_date'].year})")
            else:
                print(f"\nNo movies found produced in {country_code}.")

            # Find top 10 popular genres by number of movies
            popular_genres = catalog.find_most_popular_genre_by_number_of_movies()
            if popular_genres:
                print(f"\nTop 10 popular genres by number of movies:")
                for genre in popular_genres:
                    print(f" - {genre['genre']}: {genre['movie_count']} movies")
            else:
                print(f"\nNo genres found.")

            # Find most frequent collaborators
            collaborators = catalog.find_most_frequent_collaborators()
            if collaborators:
                print(f"\nMost frequent collaborators:")
                for record in collaborators:
                    print(f" - Actor: {record['actor']}, Director: {record['director']}, Collaborations: {record['collaborations']}")
            else:
                print(f"\nNo collaborators found.")

            # Find movies where the director also acted in
            movies = catalog.find_movies_where_director_acted()
            if movies:
                print(f"\nMovies where the director also acted:")
                for movie in movies:
                    print(f" - \"{movie['title']}\" ({movie['release_date'].year}) by {movie['person']}")
            else:
                print(f"\nNo movies found where the director also acted.")

            # Linking actor to movie
            actor_name = "Leonardo DiCaprio"
            movie_title = "Avatar"
            if catalog.link_actor_to_movie(actor_name, movie_title):
                print(f"\nLinked actor {actor_name} to movie {movie_title}.")
            else:
                print(f"\nFailed to link actor {actor_name} to movie {movie_title}.")

            # Unlinking actor from movie
            if catalog.unlink_actor_from_movie(actor_name, movie_title):
                print(f"\nUnlinked actor {actor_name} from movie {movie_title}.")
            else:
                print(f"\nFailed to unlink actor {actor_name} from movie {movie_title}.")

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
