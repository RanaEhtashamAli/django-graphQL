import graphene

from api.queries import MovieQuery


class MasterQuery(MovieQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=MasterQuery)
