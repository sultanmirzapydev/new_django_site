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

class Mutation(graphene.ObjectType):
	create_card = CreateCard.Field()
