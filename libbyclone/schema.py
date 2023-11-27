from graphene import Schema, ObjectType
import catalog.schema
import users.gql.schema
import reviews.gql.schema


class Query(catalog.schema.Query, users.gql.schema.Query, ObjectType):
    # this class will inherit from multiple queries
    # as we begin to add more apps to our project
    pass


class Mutation(catalog.schema.Mutation, users.gql.schema.Mutation, reviews.gql.schema.Mutation, ObjectType):
    # this class will inherit from multiple Mutations
    # as we begin to add more apps to our project
    pass

# 1. The above schema acts as an entry point to access GraphQL data, through Query and Mutation classes
# 2. The schema's type system allows us to define what object types are available on the backend


schema = Schema(query=Query, mutation=Mutation)
