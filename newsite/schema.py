import graphene

from users.schema import UserQuery
from survey.schema import ChoiceQuery, FeedbackQuery
from decks.schema import DeckQuery, DeckMutation

from cards.schema import CardQuery, CardMutation, DeckCardsQuery, CardUpdate




class Query(FeedbackQuery, DeckCardsQuery, CardQuery, ChoiceQuery, DeckQuery, UserQuery, graphene.ObjectType):
    pass


class Mutation(CardMutation, DeckMutation, CardUpdate, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)