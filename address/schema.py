import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from .types import *
from django.contrib.auth.models import User
import graphql_jwt
from graphql_jwt.decorators import login_required
from .mutations import * 
from .models import *
from django_filters import FilterSet
from users.types import UserType

class AddressFilter(FilterSet):
    class Meta:
        model = Address
        fields = {"userid":["exact"]}

class Query(object):
    getUserAddress = DjangoFilterConnectionField(AddressType, filterset_class=AddressFilter) 

class Mutation(object):
    addAddress = AddAddressMutation.Field()