import graphene
import graphql_jwt


from users.schema import UserQuery, UserMutation
from survey.schema import ChoiceQuery, FeedbackQuery
from decks.schema import DeckQuery, DeckMutation, DeckUpdate

from cards.schema import CardQuery, CardMutation, DeckCardsQuery, CardUpdate




class Query(FeedbackQuery, DeckCardsQuery, CardQuery, ChoiceQuery, DeckQuery, UserQuery, graphene.ObjectType):
    pass


class Mutation(CardMutation, DeckMutation, UserMutation, CardUpdate, DeckUpdate, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)