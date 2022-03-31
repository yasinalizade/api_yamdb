from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from reviews.models import Category, Comment, Genre, Review, Title
from .serializers import CategorySerializer, CommentSerializer
from .serializers import GenreSerializer, ReviewSerializer, TitleSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

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
