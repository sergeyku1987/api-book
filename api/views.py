from rest_framework.viewsets import ModelViewSet

from books.models import Book, Category
from books.serializers import BookSerializer, CategorySerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
