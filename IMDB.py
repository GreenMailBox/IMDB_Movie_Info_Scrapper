from imdb import Cinemagoer
import csv
from imdb._exceptions import IMDbDataAccessError
import os
import time

# Create an instance of the Cinemagoer class
ia = Cinemagoer()

# Prompt user for input CSV file name
input_csv_file = input("Enter the name of the input CSV file (e.g., 'horror_movies.csv'): ")

# Prompt user for output CSV file name
output_csv_file = input("Enter the name of the output CSV file (e.g., 'movie_info.csv'): ")

# Open a file to write the output
with open(output_csv_file, 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # Check if output CSV file is empty or doesn't exist
    if not os.path.isfile(output_csv_file) or os.stat(output_csv_file).st_size == 0:
        writer.writerow(['Title', 'Rating', 'Votes', 'Genres'])

    # Read existing movie titles from output CSV file
    existing_titles = set()
    with open(output_csv_file, newline='', encoding='utf-8') as moviefile:
        reader = csv.reader(moviefile)
        next(reader, None)  # Skip header row
        for row in reader:
            existing_titles.add(row[0])

    # Read movie titles from input CSV file
    with open(input_csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            title = row[0]
            if title in existing_titles:
                print("Skipping:", title, "- Already exists in", output_csv_file)
                continue  # Skip if movie already exists
            print("Searching for:", title)
            try:
                # Search for the movie
                movie_info = None
                retries = 3  # Number of retries
                for _ in range(retries):
                    try:
                        movie_info = ia.search_movie(title)
                        break  # Break out of loop if search is successful
                    except IMDbDataAccessError as e:
                        print("Error accessing IMDb data:", e)
                        print("Retrying after 5 seconds...")
                        time.sleep(5)
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
