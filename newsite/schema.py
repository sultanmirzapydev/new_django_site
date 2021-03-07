import graphene

import users.schema
from survey.schema import ChoiceQuery,FeedbackQuery


class Query(users.schema.Query, FeedbackQuery, ChoiceQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)

