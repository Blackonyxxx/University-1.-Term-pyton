movie_data = [
    {"title": "Inception", "year": 2010, "genre": "Sci-Fi", "rating": 8.7},
    {"title": "Titanic", "year": 1997, "genre": "Romance", "rating": 7.8},
    {"title": "Godfather", "year": 1972, "genre": "Crime", "rating": 9.2},
    {"title": "Dark Knight", "year": 2008, "genre": "Crime", "rating": 9.0},
    {"title": "Truman Show", "year": 1998, "genre": "Comedy", "rating": 8.2},
    {"title": "Fargo", "year": 1996, "genre": "Thriller", "rating": 8.1},
    {"title": "V for Vandetta", "year": 2005, "genre": "Action", "rating": 8.2},
    {"title": "Mad Max", "year": 2015, "genre": "Action", "rating": 8.1},
    {"title": "Alaaddin", "year": 1992, "genre": "Animation", "rating": 8.0},
    {"title": "Wonka", "year": 2023, "genre": "Adventure", "rating": 7.3},
    {"title": "Rabel Moon", "year": 2023, "genre": "Action", "rating": 5.7},
    {"title": "The Holiday", "year": 2006, "genre": "Romance", "rating": 6.9},
]

# Function to load data
def load_data():
    return movie_data
    
# Function to calculate basic statistics
def basic_statistics(movies):
    totalMovies=len(movies)
    totalRating = 0
    for movie in movies:
        totalRating = totalRating+movie['rating']
    avgRating=totalRating/totalMovies
    print("Basic Statistics: ")
    print("Total number of movies: ",totalMovies)
    print(f"Average user rating for all movies: {avgRating: .1f}")
    print("")

# Function for genre analysis
def genre_analysis(movies):
    genreCounter={}
    for movie in movies:
        genre=movie['genre']
        if genre in genreCounter:
             genreCounter[genre] += 1
        else:
            genreCounter[genre]=1
    mostCommonGenre = max(genreCounter, key=genreCounter.get)
    print ("Genre Analysis:")
    for genre, count in genreCounter.items():
        print(f"{genre}: {count} movie")
    print("Most common genre:", mostCommonGenre)
    print("")
    
# Function for yearly analysis
def yearly_analysis(movies):
    yearCounter={}
    for movie in movies:
        year=movie['year']
        if year in yearCounter:
             yearCounter[year] += 1
        else:
            yearCounter[year]=1
    mostCommonYear = max(yearCounter, key=yearCounter.get)
    print ("Year Analysis:")
    for year, count in yearCounter.items():
        print(f"{year}: {count} movie")
    print("Most common year:", mostCommonYear)
    print("")

# Function to find top-rated movies
def top_rated_movies(movies):
    def sorting(movie):
        return movie['rating']
    movies.sort(key=sorting, reverse=True)
    print("Top 5 Movies: ")
    for i in range(5):
        film = movies[i]
        print(f"{i + 1}. {film['title']} ({film['year']}) - {film['genre']} - Puan: {film['rating']}")
    print("")

# Function for user interaction
def user_interaction(movies):
    print("User Interaction:")
    title=input("Enter a movie title: ")
    
    for movie in movies:
        if movie['title'].lower() == title.lower():
            print("Movie found!")
            print(f"Title: {movie['title']}")
            print(f"Year: {movie['year']}")
            print(f"Genre: {movie['genre']}")
            print(f"Rating: {movie['rating']}")
            return
    print("This movie is not in the dataset.")

# Main Program
if __name__ == "__main__":
    # Load Data
    movie_data = load_data()

    # Basic Statistics
    basic_statistics(movie_data)

    # Genre Analysis
    genre_analysis(movie_data)

    # Yearly Analysis
    yearly_analysis(movie_data)

    # Top-Rated Movies
    top_rated_movies(movie_data)

    # User Interaction
    user_interaction(movie_data)


