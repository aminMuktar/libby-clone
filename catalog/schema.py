from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from catalog.filters import BookFilter
from catalog.models import Author, Book
from catalog.api.serializers import BookSerializer
from graphene_django.rest_framework.mutation import SerializerMutation
# each object becomes a "node"


class BookNode(DjangoObjectType):
    class Meta:
        model = Book

        interfaces = (relay.Node, )


class AuthorNode(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = []
        interfaces = (relay.Node, )

# Queries can fetch nodes using a connectionField (with filters)


class Query(ObjectType):
    book = relay.Node.Field(BookNode)
    books = DjangoFilterConnectionField(BookNode, filterset_class=BookFilter)
    author = relay.node.Field(AuthorNode)
    authors = DjangoFilterConnectionField(AuthorNode)


class BookMutation(SerializerMutation):
    class Meta:
        serializer_class = BookSerializer


class Mutation(ObjectType):
    book_mutation = BookMutation.Field()
