# we need to import get_user_model to get the user model
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
import graphene
# from users.models import CustomUser as UserModel
#from django.contrib.auth.models import User as UserModel
from graphql_auth import mutations




# This code is to make the get_user_model to grphql type
class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

# This code is used for showing the output 
class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    #  Field that we want to pass as argument to create a new user
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    # This is where the backend  logic happens  in order to crate a new user
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
	

# This class is use for making query of all the users
class UserQuery(graphene.ObjectType):
    users = graphene.List(UserType)
    me    = graphene.Field(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()
        # To get the user who is logged in for graphql api
    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user

# This class is used to register new user or verify or update user
class AuthMutation(graphene.ObjectType):
	# To create a new user from Graphql interface
	register = mutations.Register.Field()
	# To verify the newly created user
	verify_account = mutations.VerifyAccount.Field()
	# To get the token for login 	
	token_auth = mutations.ObtainJSONWebToken.Field()
	# To update the account
	update_account = mutations.UpdateAccount.Field()
	# If for some reason the user was unble to received the verification email, then we need this code to send it again
	resend_activation_email = mutations.ResendActivationEmail.Field()
	# For changing the user's password, we need to send an email to the user
	send_password_reset_email = mutations.SendPasswordResetEmail.Field()
	# Finally, this code is used to reset the password
	password_reset = mutations.PasswordReset.Field()
