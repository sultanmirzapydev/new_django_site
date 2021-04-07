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



class CreateDeck(graphene.Mutation):
	deck = graphene.Field(DeckType)

	class Arguments:
		title = graphene.String() 
		description = graphene.String()
		

	def mutate(self, info, title, description):
		deck_mutate = Deck(title=title, description=description)
		
		deck_mutate.save()
		return CreateDeck(deck=deck_mutate)

class DeckMutation(graphene.ObjectType):
	create_deck = CreateDeck.Field()
