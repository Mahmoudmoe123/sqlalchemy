from models import Movie, db

class MovieRepository:

    def get_all_movies(self):
        # Get all movies from the DB
        movies = Movie.query.all()
        return movies

    def get_movie_by_id(self, movie_id):
        # Get a single movie from the DB using the ID
        movie = Movie.query.get(movie_id)
        return movie

    def create_movie(self, title, director, rating):
        # Create a new movie in the DB
        new_movie = Movie(title=title, director=director, rating=rating)
        db.session.add(new_movie)
        db.session.commit()
        return new_movie

    def search_movies(self, title):
        # Get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        movies = Movie.query.filter(Movie.title.ilike(f"%{title}%")).all()
        return movies

# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
