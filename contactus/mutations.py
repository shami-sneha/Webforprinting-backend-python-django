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

class AddContactusMutation(relay.ClientIDMutation):
    details = graphene.Field(ContactusType)

    class Input:       
        fullname = graphene.String(required=True)
        email = graphene.String(required=True)
        enquiryabout = graphene.String()
        description = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, fullname=None, email=None, enquiryabout=None, description=None ):
        contactusObj = Contactus.objects.create(fullname=fullname, email=email, enquiryabout=enquiryabout, description=description)
        return AddContactusMutation(details=contactusObj)