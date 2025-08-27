import os
from dotenv import load_dotenv
from app.db.neo4j_client import Neo4jClient


def main():
    try:
        load_dotenv()

        neo4j_uri = os.getenv("NEO4J_URI")
        neo4j_user = os.getenv("NEO4J_USER")
        neo4j_password = os.getenv("NEO4J_PASSWORD")

        client = Neo4jClient(neo4j_uri, neo4j_user, neo4j_password)

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()