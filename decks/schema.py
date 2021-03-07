from graphene_django import DjangoObjectType
import graphene
from .models import Deck

class DeckType(DjangoObjectType):
	class Meta:
		model = Deck

class DeckQuery(graphene.ObjectType):
	decks = graphene.List(DeckType)
	def resolve_decks(self, info, **kwargs):
		return Deck.objects.all()


# schema = graphene.Schema(query=Query)
