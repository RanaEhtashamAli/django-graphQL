import graphene

from api.models import Movie
from api.schema import MovieType


class MovieQuery(graphene.ObjectType):
    all_movies = graphene.List(MovieType)

    def resolve_all_movies(self, info, **kwargs):
        return Movie.objects.all()
