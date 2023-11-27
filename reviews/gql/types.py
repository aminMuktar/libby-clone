from graphene_django import DjangoObjectType
from graphene import InputObjectType, String, Int, ID
from reviews.models import Review


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review
        convert_choices_to_enum = False


class ReviewInputType(InputObjectType):
    id = ID()
    user = ID()
    book = ID()
    comment = String()
    value = Int()
