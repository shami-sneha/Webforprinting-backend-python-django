from django.contrib.auth.models import User, Group
from graphene_django.types import DjangoObjectType
from graphene import relay
from .models import *


class CartType(DjangoObjectType):    
    class Meta:
        model = Cart
        filter_fields ='__all__'
        interfaces = (relay.Node,)


class CartItemType(DjangoObjectType):    
    class Meta:
        model = CartItem
        filter_fields ='__all__'
        interfaces = (relay.Node,)