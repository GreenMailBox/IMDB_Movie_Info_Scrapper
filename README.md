# IMDB_Movie_Info_Scrapper
IMDB_Movie_Info_Scrapper

# IMDb Movie Info Scraper
This Python script retrieves information about movies from IMDb using the IMDbPY library. It reads a list of movie titles from a CSV file, searches for each title on IMDb, and extracts details such as rating, votes, and genres. The retrieved information is then saved to another CSV file.

This Script is intended to be used after the genre.py script created: as the genre.py script will get a list of all movies within a category
you can alternativly use your own list of moveies and get infromation 

Note: this may potentially get your IP blocked by IMDB: due to high volume of traffic 

## Features

- Retrieves movie information from IMDb
- Handles existing movie titles to avoid duplicates in the output CSV file
- Provides error handling for cases where IMDb data access fails
- Saves movie information to a CSV file for easy access and analysis

## Prerequisites

- Python 3.x
- `imdbpy` library

## Installation

1. Clone the repository:
git clone https://github.com/your-username/imdb-movie-info-scraper.git


2. Install the IMDbPY library:
pip install IMDbPY

## Usage

1. Prepare a CSV file (`horror_movies.csv`) containing a list of movie titles.
2. Run the script:

python imdb_scraper.py
3. The script will search IMDb for each movie title in the CSV file, retrieve the desired information, and append it to a new CSV file (`movie_info.csv`).

## Example CSV Format
Title,Rating,Votes,Genres
No Way Up,4.6,4185,"Action, Adventure, Drama, Thriller"
Immaculate,5.9,20476,Horror


## Contributors
Joshua Hemingway

## License
This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.

