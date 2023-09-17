from graphene_django.types import DjangoObjectType

from api.models import Movie


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
