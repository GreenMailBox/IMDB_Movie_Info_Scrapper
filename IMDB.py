from imdb import Cinemagoer
import csv
from imdb._exceptions import IMDbDataAccessError
import os

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# Open a file to write the output
with open('movie_info.csv', 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # Check if movie_info.csv is empty or doesn't exist
    if not os.path.isfile('movie_info.csv') or os.stat('movie_info.csv').st_size == 0:
        writer.writerow(['Title', 'Rating', 'Votes', 'Genres'])

    # Read existing movie titles from movie_info.csv
    existing_titles = set()
    with open('movie_info.csv', newline='', encoding='utf-8') as moviefile:
        reader = csv.reader(moviefile)
        next(reader, None)  # Skip header row
        for row in reader:
            existing_titles.add(row[0])

    # Read movie titles from CSV file
    with open('horror_movies.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            title = row[0]
            if title in existing_titles:
                print("Skipping:", title, "- Already exists in movie_info.csv")
                continue  # Skip if movie already exists
            print("Searching for:", title)
            try:
                # Search for the movie
                movie_info = ia.search_movie(title)
                if movie_info:
                    # Get the first movie in the search results
                    movie_id = movie_info[0].movieID
                    # Get detailed information about the movie
                    movie = ia.get_movie(movie_id)
                    # Write movie title, rating, votes, and genres to the file
                    writer.writerow([movie['title'], movie.get('rating'), movie.get('votes'), ', '.join(movie.get('genres', []))])
                else:
                    writer.writerow([title, "Not Found", "", ""])
            except IMDbDataAccessError as e:
                writer.writerow([title, "Error accessing IMDb data", "", ""])
            # Flush the buffer to ensure data is written to file
            csvfile.flush()
