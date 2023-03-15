class Movie:
    """A movie holds a title, director, and rating"""

    def __init__(self, title: str, director: str, rating: int) -> None:
        self.title = title
        self.director = director
        self.rating = rating

    #added getters for part 1
    def getTitle(self) -> str:
        return self.title
    
    def getDirector(self) -> str:
        return self.director
    
    def getRating(self) -> str:
        return self.rating
    