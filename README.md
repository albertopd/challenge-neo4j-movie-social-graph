# Challenge Neo4j Movie Social Graph

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/) ![pandas](https://img.shields.io/badge/pandas-2.3.2-150458.svg?logo=pandas) ![Neo4j](https://img.shields.io/badge/neo4j-5.28.2-008CC1.svg?logo=neo4j)

This project models a social graph of movies, capturing the complex relationships between films, actors, directors, genres, and other entities using Neo4j. It enables interactive exploration and analysis of collaborations, connections, and trends within the movie industry.

## ✨ Features

- Import movies and credits from CSV files
- Transform and normalize movie and credit data
- Store movies, genres, keywords, companies, countries, languages, cast, and crew in Neo4j
- Query movies by director, actors, genre, keywords, country, and popularity
- Analyze collaborations and relationships between actors and directors
- Link and unlink actors to movies interactively

## 📂 Project Structure

```
challenge-neo4j-movie-social-graph/
├── app/
│   ├── db/
│   │   └── movies_catalog.py       # Neo4j database interaction and queries
│   ├── pipelines/
│   │   ├── transform_movies.py     # Data transformation for movies
│   │   └── transform_credits.py    # Data transformation for credits
│   └── utils/
│       └── parse_helpers.py        # Helper functions for parsing data
├── data/
│   ├── tmdb_5000_movies.csv        # Source movie data (must be downloaded manually)
│   ├── tmdb_5000_credits.csv       # Source credits data (must be downloaded manually)
│   └── README.md                   # Documentation about how to download the CSV file
├── .env                            # Local environment variables
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
└── LICENSE                         # License information
```

## 📋 Requirements

- Python 3.13 or later
- Neo4j database (local or remote)
- Required Python packages listed in [requirements.txt](requirements.txt)

## 📦 Installation

1. Clone the repository:
	 ```sh
	 git clone https://github.com/albertopd/challenge-neo4j-movie-social-graph.git
	 cd challenge-neo4j-movie-social-graph
	 ```
2. Install dependencies:
	 ```sh
	 pip install -r requirements.txt
	 ```
3. Set up a Neo4j database and note your connection URI, username, password, and database name.

## ⚙️ Configuration

Create a `.env` file in the root of the project and add your Neo4j connection details:

```
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password
NEO4J_DB_NAME=movies
MOVIES_DATASET_CSV_PATH=data/tmdb_5000_movies.csv
CREDITS_DATASET_CSV_PATH=data/tmdb_5000_credits.csv
```

## 🚀 Usage

1. Start your Neo4j database.
2. Run the main script:
   ```sh
   python -m app.main
   ```

## 📜 License

This project is licensed under the [MIT License](LICENSE).

## 👤 Author

[Alberto Pérez Dávila](https://github.com/albertopd)