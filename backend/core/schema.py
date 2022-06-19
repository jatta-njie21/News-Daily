import graphene
from graphene import ObjectType
from authors import schema


class Query(schema.Query, ObjectType):
    pass


schema = graphene.Schema(query = Query)