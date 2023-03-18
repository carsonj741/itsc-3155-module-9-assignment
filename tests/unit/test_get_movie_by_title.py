# TODO: Feature 3
from src.repositories.movie_repository import MovieRepository
from src.models.movie import Movie

def test_get_movie_by_title():
    movies = MovieRepository()
    assert None == movies.get_movie_by_title("Star Wars")
    movies.create_movie("Star Wars", "George Lucas", 5)
    foundTitle = movies.get_movie_by_title("Star Wars")
    assert foundTitle.title == "Star Wars"
    assert foundTitle.director == "George Lucas"
    assert foundTitle.rating == 5
