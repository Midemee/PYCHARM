from movie_rating.movie import Movie
from datetime import datetime

class MovieRating:
    def __init__(self):
        self.movies = []

    def add_movie(self , title: str, year, director, genre):
        title = title.lower()
        mv = Movie(title,year,director,genre)
        self.movies.append(mv)

    def get_movies(self):
        return self.movies

    def get_movie_date(self, date):
        current_date = datetime.now()
        return current_date

    def rate_movie(self, title: str, rating: int) -> None:
        if rating < 0 or rating > 5:
            raise ValueError("Rating must be between 0 and 5")
        for movie in self.movies:
            if movie.title == title.lower():
                movie.rating.append(rating)

    def get_rating(self):
        for movie in self.movies:
            return movie.rating
        return None


        # if rate < 1 or rate > 5:
        #     return "Invalid rate"
        # return rate
