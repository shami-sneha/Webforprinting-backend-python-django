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

class AddAddressMutation(relay.ClientIDMutation):
    details = graphene.Field(AddressType)

    class Input:
        userid = graphene.ID(required=True)
        countryid = graphene.String(required=True)
        state = graphene.ID()
        city = graphene.String(required=True)
        pincode = graphene.String(required=True)
        fullname = graphene.String(required=True)
        phonenumber = graphene.String(required=True)
        addressline1 = graphene.String(required=True)
        addressline2 = graphene.String()
        instructions = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, userid=None, countryid=None, state=None, city=None, pincode=None, fullname=None, phonenumber=None, addressline1=None, addressline2=None, instructions=None):
        userObj = User.objects.get(id=from_global_id(userid)[1])
        # state = States.objects.get(id=from_global_id(state)[1])
        addressObj = Address.objects.create(userid=userObj, countryid=countryid, city=city, pincode=pincode, fullname=fullname, phonenumber=phonenumber, addressline1=addressline1, addressline2=addressline2, instructions=instructions)

        return AddAddressMutation(details=addressObj)