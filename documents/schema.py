import graphene
from graphene import relay,ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .types import *
from django.contrib.auth.models import User
import graphql_jwt
from graphql_jwt.decorators import login_required
from .mutations import * 
from .models import *
from django_filters import FilterSet
from users.types import UserType
from documents.types import DocumnetsType

class DocumnetsFilter(FilterSet):
    class Meta:
        model = Documents
        fields = {"docType":["exact"]}

class Query(graphene.ObjectType):
      print(DocumnetsType)
      getUserDocuments=DjangoFilterConnectionField(DocumnetsType,filterset_class=DocumnetsFilter)



 