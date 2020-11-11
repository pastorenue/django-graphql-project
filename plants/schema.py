import graphene
from graphene_django import DjangoObjectType

from .models import Plant, Species

class SpeciesObjectType(DjangoObjectType):
    class Meta:
        model = Species
        fields = "__all__"


class PlantObjectType(DjangoObjectType):
    class Meta:
        model = Plant
        fields = ("id", "name", "species")
    added_field = graphene.String()

    def resolve_added_field(self, info):
        return info.context.user.is_authenticated()
 
   
class Query(graphene.ObjectType):
    species = graphene.List(SpeciesObjectType)
    species_by_id = graphene.Field(SpeciesObjectType, id=graphene.String())
    
    # Plant Queries
    plants = graphene.List(PlantObjectType)
    plant_by_id = graphene.Field(PlantObjectType, id=graphene.String())
    
    # Define all resolvers
    def resolver_species(root, info):
        return Species.objects.all()

    def resolve_plant_by_id(root, info, id):
        return Species.objects.get(id=id)

    def resolve_plants(root, info):
        return Plant.objects.all()
    
        