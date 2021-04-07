from django.contrib.auth import get_user_model

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


# To create a new user from the Graphql api





#class UserType(DjangoObjectType):
   # class Meta:
      #  model = get_user_model()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class UserMutation(graphene.ObjectType):
    create_user = CreateUser.Field()