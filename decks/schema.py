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



# To update any particular deck, this code is useful

class UpdateDeck(graphene.Mutation):
	deck = graphene.Field(DeckType)

	class Arguments:
		title       = graphene.String()
		description = graphene.String()
		deck_id     = graphene.Int()

		
	def mutate(self, info, description, title, deck_id):
		deck_update = Deck.objects.get(id=deck_id)

		
		deck_update.title = title
		deck_update.description = description
		deck_update.save()

		return UpdateDeck(deck=deck_update)

class DeckUpdate(graphene.ObjectType):
	update_deck =  UpdateDeck.Field()