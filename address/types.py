from django.contrib.auth.models import User, Group
from graphene_django.types import DjangoObjectType
from graphene import relay
from .models import *


class AddressType(DjangoObjectType):    
    class Meta:
        model = Address
        filter_fields ='__all__'
        interfaces = (relay.Node,)