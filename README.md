# Neo4j Movie Social Graph

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

## 📝 Example Output

```sh
Setting up catalog...
Populating catalog with movies from CSV file: data/tmdb_5000_movies.csv ...
Processing chunk 1 out of 25 : 200 rows
Processing chunk 2 out of 25 : 200 rows
...
Processing chunk 25 out of 25 : 3 rows
Catalog populated with 4803 movies.
Populating catalog with credits from CSV file: data/tmdb_5000_credits.csv ...
Processing chunk 1 out of 25 : 200 rows
Processing chunk 2 out of 25 : 200 rows
...
Processing chunk 25 out of 25 : 3 rows
Catalog populated with 4803 credits.
Catalog setup complete.

Movies directed by Christopher Nolan:
 - "Interstellar" (2014)
 - "The Dark Knight Rises" (2012)
 - "Inception" (2010)
 - "The Dark Knight" (2008)
 - "The Prestige" (2006)
 - "Batman Begins" (2005)
 - "Insomnia" (2002)
 - "Memento" (2000)

Movies featuring Chris Evans, Chris Hemsworth:
 - "Avengers: Age of Ultron" (2015)
 - "Thor: The Dark World" (2013)
 - "The Avengers" (2012)

Movies in the Fantasy genre (after 2010):
 - "Pete's Dragon" (2016)
 - "Suicide Squad" (2016)
 - "Ghostbusters" (2016)
 - "Sausage Party" (2016)
 - "Yoga Hosers" (2016)
 - "Teenage Mutant Ninja Turtles: Out of the Shadows" (2016)
 - "The BFG" (2016)
 - "Alice Through the Looking Glass" (2016)
 - "Warcraft" (2016)
 - "The Jungle Book" (2016)

Movies produced in country: CA:
 - "Sausage Party" (2016)
 - "The Legend of Tarzan" (2016)
 - "Now You See Me 2" (2016)
 - "Warcraft" (2016)
 - "The Conjuring 2" (2016)
 - "My Big Fat Greek Wedding 2" (2016)
 - "Race" (2016)
 - "The Witch" (2016)
 - "The Boy" (2016)
 - "The Revenant" (2015)

Top 10 popular genres by number of movies:
 - Drama: 2297 movies
 - Comedy: 1722 movies
 - Thriller: 1274 movies
 - Action: 1154 movies
 - Romance: 894 movies
 - Adventure: 790 movies
 - Crime: 696 movies
 - Science Fiction: 535 movies
 - Horror: 519 movies
 - Family: 513 movies

Most frequent collaborators:
 - Actor: Danny Trejo, Director: Robert Rodriguez, Collaborations: 10
 - Actor: Antonio Banderas, Director: Robert Rodriguez, Collaborations: 8
 - Actor: Giannina Facio, Director: Ridley Scott, Collaborations: 8
 - Actor: Cheech Marin, Director: Robert Rodriguez, Collaborations: 8
 - Actor: Héctor Elizondo, Director: Garry Marshall, Collaborations: 8
 - Actor: Jason Mewes, Director: Kevin Smith, Collaborations: 8
 - Actor: Jennifer Schwalbach Smith, Director: Kevin Smith, Collaborations: 7
 - Actor: Robert De Niro, Director: Martin Scorsese, Collaborations: 7
 - Actor: Jason Lee, Director: Kevin Smith, Collaborations: 7
 - Actor: Dick Miller, Director: Joe Dante, Collaborations: 7

Movies where the director also played a character:
 - "Growing Up Smith" (2017) by Frank Lotito as Officer Bob
 - "Two Lovers and a Bear" (2016) by Kim Nguyen as Roman
 - "Mr. Church" (2016) by Bruce Beresford as Henry Church
 - "The Birth of a Nation" (2016) by Nate Parker as Samuel Turner
 - "Kicks" (2016) by Justin Tipping as Marlon
 - "Antibirth" (2016) by Danny Perez as Warren
 - "Hands of Stone" (2016) by Jonathan Jakubowicz as Chaflan
 - "Ben-Hur" (2016) by Timur Bekmambetov as Sheik Ilderim
 - "Pete's Dragon" (2016) by David Lowery as Grace Meacham
 - "Suicide Squad" (2016) by David Ayer as Firefighter

Linked actor Leonardo DiCaprio to movie Avatar.

Unlinked actor Leonardo DiCaprio from movie Avatar.
```

## 📜 License

This project is licensed under the [MIT License](LICENSE).

## 👤 Author

[Alberto Pérez Dávila](https://github.com/albertopd)
