import graphene
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations
import graphql_jwt


class AuthMutation(graphene.ObjectType):
   register = mutations.Register.Field()


class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)