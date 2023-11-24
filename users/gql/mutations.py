from graphene import Field, Mutation, String
from django.contrib.auth import get_user_model
from .types import UserType

User = get_user_model()


class UserCreate(Mutation):
    # 1. Declare the mutations result field
    user = Field(UserType)

    # 2. Declare arguments for the mutation
    class Arguments:
        username = String(required=True)
        password = String(required=True)
        email = String(required=True)

    def mutate(self, info, username, password, email):
        user = User(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()

        return UserCreate(user=user)
