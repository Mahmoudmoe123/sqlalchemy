class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB
        return None

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        return None

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        return None

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        return None


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
