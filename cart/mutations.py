import graphene
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from graphql_relay import from_global_id
from graphene import relay
from .types import *
import datetime
from django.contrib.auth.models import User
from graphql import GraphQLError
from users.types import UserType

class AddCartMutation(relay.ClientIDMutation):
    details = graphene.Field(CartType)

    class Input:
         userid=graphene.ID()
         status = graphene.String(required=True) 


    @classmethod
    def mutate_and_get_payload(cls, root, info,userid=None, status=None):
        userObj = User.objects.get(id=from_global_id(userid)[1])
        print(userObj)
        cartObj = Cart.objects.create(userid=userObj, status=status)
        return AddCartMutation(details=cartObj)



class DeleteCartMutation(graphene.Mutation):

    class Input:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()
    delivery_owner = graphene.Field(CartType)

    def mutate(self, info,id=None):
        id = from_global_id(id)[1]
        cartObj = Cart.objects.filter(id=id).delete()
        ok = True
        return DeleteCartMutation(ok=ok)


class AddCartItemMutation(relay.ClientIDMutation):
    details = graphene.Field(CartItemType)

    class Input:
        cartid = graphene.ID()
        productid = graphene.ID()
        photoid = graphene.ID(required=False)
        documentid = graphene.ID(required=False)


    @classmethod
    def mutate_and_get_payload(cls, root, info,cartid=None, productid=None, photoid=None, documentid=None):
        cartObj = Cart.objects.get(id=from_global_id(cartid)[1])
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa........................")
        productObj = Products.objects.get(id=from_global_id(productid)[1])
        cartItemObj = CartItem(cartid=cartObj, productid=productObj)
        if photoid is not None:
            photoObj = Photos.objects.get(id=from_global_id(photoid)[1])
            cartItemObj.photoid=photoObj
        if documentid is not None:
            DocumentObj = Documents.objects.get(id=from_global_id(documentid)[1])
            cartItemObj.documentid=DocumentObj
        cartItemObj.save()
        return AddCartItemMutation(details=cartItemObj)

class DeleteCartItemMutation(graphene.Mutation):

    class Input:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()
    delivery_owner = graphene.Field(CartItemType)

    def mutate(self, info,id=None):
        id = from_global_id(id)[1]
        cartItemObj = CartItem.objects.filter(id=id).delete()
        ok = True
        return DeleteCartItemMutation(ok=ok)