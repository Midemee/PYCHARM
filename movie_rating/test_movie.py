from movie_rating.movie import Movie
from movie_rating.movie_rating import MovieRating

class TestMovie:
    def setUp(self):
        self.mvr = MovieRating()
        self.mvr.add_movie("koto aye", "2000", "Azeez", "horror")
    def test_movie(self):
        Movie("koto aye", "2000", "Azeez",  "horror")

    class TestRating:
        def test_add_movie(self):
            mvr = MovieRating()
            assert len(mvr.movies) == 0
            mvr.add_movie("koto aye", "2000", "Azeez", "horror")
            assert len(mvr.movies) == 1

        def test_rate_movie(self):
            mvr = MovieRating()
            assert len(mvr.movies) == 0
            mvr.add_movie("koto aye", "2000", "Azeez", "horror")
            assert len(mvr.get_rating()) == 0
            mvr.rate_movie("koto aye", 5)
            assert len(mvr.get_rating()) == 1
            mvr.rate_movie("koto aye", 5)
            assert len(mvr.get_rating()) == 2
