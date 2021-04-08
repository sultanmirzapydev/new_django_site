from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
import graphene
# from users.models import CustomUser as UserModel
#from django.contrib.auth.models import User as UserModel
from graphql_auth import mutations





class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


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
	

class UserQuery(graphene.ObjectType):
    users = graphene.List(UserType)
    me    = graphene.Field(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user


class AuthMutation(graphene.ObjectType):
	# To create a new user from Graphql interface
	register = mutations.Register.Field()
	verify_account = mutations.VerifyAccount.Field()
	token_auth = mutations.ObtainJSONWebToken.Field()
	update_account = mutations.UpdateAccount.Field()
	resend_activation_email = mutations.ResendActivationEmail.Field()
	send_password_reset_email = mutations.SendPasswordResetEmail.Field()
	password_reset = mutations.PasswordReset.Field()
