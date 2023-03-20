# TODO: Feature 1

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from src.repositories.movie_repository import movie_repository
from src.models.movie import Movie

def test_get_all_movies_method():
    movies = [Movie("The Shawshank Redemption", "Frank Darabont", 4), Movie("The Godfather", "Francis Ford Coppola", 1), Movie("The Room", "Tommy Wiseau", 5)]
    movie_repository.create_movie("The Shawshank Redemption", "Frank Darabont", 4)
    movie_repository.create_movie("The Godfather", "Francis Ford Coppola", 1)
    movie_repository.create_movie("The Room", "Tommy Wiseau", 5)
    movies = movie_repository.get_all_movies()
    
    for movie in range(3):
        assert type(movies[movie]) is Movie
        assert movies[movie].title == movies[movie].title
        assert movies[movie].director == movies[movie].director
        assert movies[movie].rating == movies[movie].rating