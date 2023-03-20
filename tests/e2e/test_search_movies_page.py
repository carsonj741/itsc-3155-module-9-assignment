# TODO: Feature 3
from app import app
from src.repositories.movie_repository import movie_repository


def test_search_movies_page():
    test_app = app.test_client()
    search = test_app.get("/movies/search")
    assert b'<p>No Results</p>' in response.data
    search = test_app.get("/movies/search?title=Star+Wars")
    assert b'<p>No Results</p>' in response.data
    movie_repository.make_movie(
    "Star Wars", "George Lucas", 5)
    search = test_app.get("/movies/search?title=Star+Wars")
    assert b'<td>Movie Found:</td>' in response.data
    assert b'<td>Star Wars</td>' in response.data
    assert b'<td>Rating:</td>' in response.data
    assert b'<td>5</td>' in response.data
