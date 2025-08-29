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


Catalog setup complete.

Movies directed by Christopher Nolan:
 - "Interstellar" (2014)
 - "The Dark Knight Rises" (2012)
 - "Inception" (2010)
 - "The Dark Knight" (2008)

Movies featuring Chris Evans, Chris Hemsworth:
 - "Avengers: Age of Ultron" (2015)
 - "The Avengers" (2012)

Movies in the Fantasy genre (after 2010):
 - "Suicide Squad" (2016)
 - "The Jungle Book" (2016)
 - "Batman v Superman: Dawn of Justice" (2016)
 - "Jupiter Ascending" (2015)
 - "The Hobbit: The Battle of the Five Armies" (2014)
 - "Maleficent" (2014)
 - "X-Men: Days of Future Past" (2014)
 - "The Amazing Spider-Man 2" (2014)
 - "The Hobbit: The Desolation of Smaug" (2013)
 - "47 Ronin" (2013)
 - "Man of Steel" (2013)
 - "Oz: The Great and Powerful" (2013)
 - "Jack the Giant Slayer" (2013)
 - "The Hobbit: An Unexpected Journey" (2012)
 - "The Amazing Spider-Man" (2012)
 - "Brave" (2012)
 - "Snow White and the Huntsman" (2012)
 - "Pirates of the Caribbean: On Stranger Tides" (2011)

Movies produced in CA:
 - "The Legend of Tarzan" (2016)
 - "Interstellar" (2014)
 - "Pacific Rim" (2013)
 - "2012" (2009)
 - "X-Men: The Last Stand" (2006)

Top 10 popular genres by number of movies:
 - Adventure: 78 movies
 - Action: 70 movies
 - Science Fiction: 43 movies
 - Fantasy: 35 movies
 - Family: 26 movies
 - Thriller: 17 movies
 - Animation: 16 movies
 - Drama: 15 movies
 - Comedy: 12 movies
 - Crime: 7 movies

Most frequent collaborators:
 - Actor: Jed Brophy, Director: Peter Jackson, Collaborations: 4
 - Actor: Michael Caine, Director: Christopher Nolan, Collaborations: 4
 - Actor: Mark Hadlow, Director: Peter Jackson, Collaborations: 4
 - Actor: Timothy Patrick Quill, Director: Sam Raimi, Collaborations: 3
 - Actor: Bruce Campbell, Director: Sam Raimi, Collaborations: 3
 - Actor: John Paxton, Director: Sam Raimi, Collaborations: 3
 - Actor: James Franco, Director: Sam Raimi, Collaborations: 3
 - Actor: Johnny Depp, Director: Gore Verbinski, Collaborations: 3
 - Actor: Russ Fega, Director: Christopher Nolan, Collaborations: 3
 - Actor: Cillian Murphy, Director: Christopher Nolan, Collaborations: 3

Movies where the director also acted:
 - "Shin Godzilla" (2016) by Hideaki Anno
 - "Captain America: Civil War" (2016) by Joe Russo
 - "The Jungle Book" (2016) by Jon Favreau
 - "The Good Dinosaur" (2015) by Peter Sohn
 - "Jurassic World" (2015) by Colin Trevorrow
 - "Inside Out" (2015) by Pete Docter
 - "Guardians of the Galaxy" (2014) by James Gunn
 - "X-Men: Days of Future Past" (2014) by Bryan Singer
 - "Captain America: The Winter Soldier" (2014) by Joe Russo
 - "Wreck-It Ralph" (2012) by Rich Moore

Linked actor Leonardo DiCaprio to movie Avatar.

Unlinked actor Leonardo DiCaprio from movie Avatar.
```

## 📜 License

This project is licensed under the [MIT License](LICENSE).

## 👤 Author

[Alberto Pérez Dávila](https://github.com/albertopd)