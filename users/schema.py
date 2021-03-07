from graphene_django import DjangoObjectType
import graphene
from users.models import User as UserModel

class User(DjangoObjectType):
    class Meta:
        model = UserModel

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info, **kwargs):
        return UserModel.objects.all()


#schema = graphene.Schema(query=Query)
