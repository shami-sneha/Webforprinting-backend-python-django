from django.contrib.auth.models import User, Group
from graphene_django.types import DjangoObjectType
from graphene import relay
from .models import *

class ContactusType(DjangoObjectType):    
    class Meta:
        model = Contactus
        filter_fields ='__all__'
        interfaces = (relay.Node,)