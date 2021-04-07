from graphene_django import DjangoObjectType
import graphene
from .models import Card
from decks.models import Deck


class CardType(DjangoObjectType):
	class Meta:
		model = Card

class CardQuery(graphene.ObjectType):
	cards = graphene.List(CardType)
	def resolve_cards(self, info, **kwargs):
		return Card.objects.all()


# This below code is to make the query for all the cards associated with a particular deck

class DeckCardsQuery(graphene.ObjectType):
	# we need to define what we want to  make query of 
	deck_cards = graphene.List(CardType, deck=graphene.Int())
# This code is to return the query
	def resolve_deck_cards(self, info, deck):
		return Card.objects.filter(deck=deck)




# To create a new card from graphql, we need below code to execute

class CreateCard(graphene.Mutation):
	card = graphene.Field(CardType)

	class Arguments:
		question = graphene.String()
		answer   = graphene.String()
		deck_id  = graphene.Int()

	def mutate(self, info, question, answer, deck_id):
		card_mutate = Card(question=question, answer=answer)
		deck_qs = Deck.objects.get(id=deck_id)
		card_mutate.deck = deck_qs
		card_mutate.save()
		return CreateCard(card=card_mutate)

class CardMutation(graphene.ObjectType):
	create_card = CreateCard.Field()


# To update any particular card we need to use this code.

class UpdateCard(graphene.Mutation):
	card = graphene.Field(CardType)

	class Arguments:
		question = graphene.String()
		answer = graphene.String()
		card_id = graphene.Int()

	def mutate(self, info, question, answer, card_id):
		card_update = Card.objects.get(id=card_id)

		#cardupdate = card_update(question=question, answer=answer)
		card_update.question = question
		card_update.answer = answer
		card_update.save()

		return UpdateCard(card=card_update)

class CardUpdate(graphene.ObjectType):
	update_card =  UpdateCard.Field()