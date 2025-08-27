from neo4j import GraphDatabase


class Neo4jClient:
    def __init__(
        self, 
        uri: str, 
        user: str, 
        password: str
    ):
        if not uri or not user or not password:
            raise ValueError("Neo4j URI, user, and password must be provided")
        self.__driver = GraphDatabase.driver(uri, auth=(user, password))
        self.__driver.verify_connectivity()

    def close(self):
        self.__driver.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
