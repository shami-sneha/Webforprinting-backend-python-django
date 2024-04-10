import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .types import *
from django.contrib.auth.models import User
import graphql_jwt
from graphql_jwt.decorators import login_required
from .mutations import * 
from .models import *
from django_filters import FilterSet
from contactus.types import ContactusType

class ContactusFilter(FilterSet):
    class Meta:
        model = Contactus
        fields = {"email":["exact"]}

class Query(graphene.ObjectType):
    #Contactus_by_email = DjangoFilterConnectionField(ContactusType, filterset_class=ContactusFilter) 
    getContactus = DjangoFilterConnectionField(ContactusType)
    def resolve_getContactus(root, info, **kwargs):
        # Querying a list
        return Contactus.objects.all()

class Mutation(object):
    addContactus = AddContactusMutation.Field()