import graphene

from users.schema import UserQuery
from survey.schema import ChoiceQuery, FeedbackQuery
from decks.schema import DeckQuery
from cards.schema import CardQuery




class Query(FeedbackQuery, CardQuery, ChoiceQuery, DeckQuery, UserQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
