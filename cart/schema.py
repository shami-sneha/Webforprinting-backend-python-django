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
from cart.types import CartType,CartItemType

class CartFilter(FilterSet):
     class Meta:
          model = Cart
          fields = {"userid":["exact"]}

class CartItemFilter(FilterSet):
     class Meta:
          model = CartItem
          fields = {"cartid":["exact"]}

class Query(graphene.ObjectType):
     print(CartType)
     getUserCart = DjangoFilterConnectionField(CartType,filterset_class=CartFilter)
     getUserCartItem = DjangoFilterConnectionField(CartItemType,filterset_class=CartItemFilter)

class Mutation(object):
     addCart = AddCartMutation.Field()
     deleteCart = DeleteCartMutation.Field()
     addCartItem = AddCartItemMutation.Field()
     deleteCartItem = DeleteCartItemMutation.Field()