from graphene_django import DjangoObjectType
import graphene
# from users.models import User as UserModel
from django.contrib.auth.models import User as UserModel

class UserType(DjangoObjectType):
	class Meta:
		model = UserModel

class UserQuery(graphene.ObjectType):
	users = graphene.List(UserType)
	def resolve_users(self, info, **kwargs):
		return UserModel.objects.all()


# schema = graphene.Schema(query=Query)
