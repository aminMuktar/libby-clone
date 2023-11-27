from graphene import Boolean, Field, ID, Mutation
from django.contrib.auth import get_user_model
from reviews.models import Review

from .types import ReviewType, ReviewInputType
from .serializers import ReviewSerializer
from graphql_jwt.decorators import login_required


User = get_user_model()


class ReviewCreate(Mutation):
    review = Field(ReviewType)

    class Arguments:
        input = ReviewInputType(required=True)

    @classmethod
    @login_required
    def mutate(cls, root, info, **data):
        user = info.context.user
        review_data = data.get('input')
        review_data['user'] = user.id

        serializer = ReviewSerializer(data=review_data)
        serializer.is_valid(raise_exception=True)
        return ReviewCreate(review=serializer.save())


class ReviewUpdate(Mutation):
    review = Field(ReviewType)

    class Arguments:
        input = ReviewInputType(required=True)

    @classmethod
    @login_required
    def mutate(cls, root, info, **data):
        user = info.context.user
        review_data = data.get('input')
        review_data['user'] = user.id

        review_instance = Review.objects.get(
            id=review_data.get('id'), user=review_data.get('user'))
        serializer = ReviewSerializer(review_instance, data=review_data)
        serializer.is_valid(raise_exception=True)
        return ReviewUpdate(review=serializer.save())


class ReviewDelete(Mutation):
    class Arguments:
        id = ID(required=True)
    ok = Boolean()

    @classmethod
    @login_required
    def mutate(cls, root, info, **data):
        user = info.context.user
        review = Review.objects.get(id=data.get('id'), user=user)
        review.delete()
        return ReviewDelete(ok=True)
