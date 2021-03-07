from graphene_django import DjangoObjectType
import graphene
from .models import Card


class CardType(DjangoObjectType):
	class Meta:
		model = Card

class CardQuery(graphene.ObjectType):
	cards = graphene.List(CardType)
	def resolve_cards(self, info, **kwargs):
		return Card.objects.all()



