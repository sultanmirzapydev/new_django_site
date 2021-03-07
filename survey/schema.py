from graphene_django import DjangoObjectType
import graphene
from .models import Choice

class ChoiceType(DjangoObjectType):
    class Meta:
        model = Choice

class ChoiceQuery(graphene.ObjectType):
    choices = graphene.List(ChoiceType)

    def resolve_Choices(self, info, **kwargs):
        return Choice.objects.all()


#schema = graphene.Schema(query=Query)


# Below code is for Feedback model

from graphene_django import DjangoObjectType
import graphene
from .models import Feedback

class FeedbackType(DjangoObjectType):
    class Meta:
        model = Feedback

class FeedbackQuery(graphene.ObjectType):
    feedbacks = graphene.List(FeedbackType)

    def resolve_feedbacks(self, info, **kwargs):
        return Feedback.objects.all()
