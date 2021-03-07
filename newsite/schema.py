import graphene

from users.schema import UserQuery
from survey.schema import ChoiceQuery, FeedbackQuery


class Query(FeedbackQuery, ChoiceQuery, UserQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
