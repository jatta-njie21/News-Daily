import graphene
import graphene_django

from graphene import ObjectType
from graphene_django import DjangoObjectType
from .models import Detail



class DetailType(DjangoObjectType):
    class Meta:
        model  = Detail
        fields = '__all__'

class Query(ObjectType):
    all_authors = graphene.List(DetailType)

    def resolve_all_authors(self,info):
        return Detail.objects.all()

