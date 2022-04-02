from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

from reviews.models import Category, Comment, Genre, Review, Title
from .filters import TitleFilter
from .serializers import (CategorySerializer, CommentSerializer,
                          GenreSerializer, ReviewSerializer,
                          TitleReadSerializer, TitleWriteSerializer)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('reviews__score')).all()
    serializer_class = TitleWriteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleReadSerializer
        return TitleWriteSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        queryset = Review.objects.all()
        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title, pk=title_id)
        return queryset.filter(title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Comment.objects.all()
        title_id = self.kwargs.get("title_id")
        review_id = self.kwargs.get("review_id")
        title = get_object_or_404(Title, pk=title_id)
        review = get_object_or_404(Review, pk=review_id)
        return queryset.filter(title=title, review=review)

    def perform_create(self, serializer, *args, **kwargs):
        title_id = self.kwargs.get("title_id")
        review_id = self.kwargs.get("review_id")
        title = get_object_or_404(Title, pk=title_id)
        review = get_object_or_404(Review, pk=review_id)
        return serializer.save(
            author=self.request.user,
            title=title,
            review=review
        )
