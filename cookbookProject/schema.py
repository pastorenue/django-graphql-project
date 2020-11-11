import graphene
import ingredients.schema
import plants.schema

class Query(plants.schema.Query, ingredients.schema.Query, graphene.ObjectType):
    # this class will inherit from multiple queries 
    # as we add more apps to the project
    pass

schema = graphene.Schema(query=Query)