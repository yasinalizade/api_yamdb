from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .mixins import ListCreateDestroyViewSet
from .filters import TitleFilter
from .permissions import (IsAdmin, IsAdminOrReadOnly,
                          IsAdminModeratorAuthorPermission)
from .serializers import (CategorySerializer, CommentSerializer,
                          GenreSerializer, ReviewSerializer,
                          TitleReadSerializer, TitleWriteSerializer,
                          NotAdminSerializer, UsersSerializer)

from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User


class CategoryViewSet(ListCreateDestroyViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
    permission_classes = (IsAdminOrReadOnly,)


class GenreViewSet(ListCreateDestroyViewSet):
    queryset = Genre.objects.all().order_by('id')
    serializer_class = GenreSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
    permission_classes = (IsAdminOrReadOnly,)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')
    ).all().order_by('id')
    serializer_class = TitleWriteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    permission_classes = (IsAdminOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleReadSerializer
        return TitleWriteSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAdminModeratorAuthorPermission,)

    def get_queryset(self, *args, **kwargs):
        queryset = Review.objects.all().order_by('id')
        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title, pk=title_id)
        return queryset.filter(title=title)

    def perform_create(self, serializer, *args, **kwargs):
        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title, pk=title_id)
        return serializer.save(
            author=self.request.user,
            title=title
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAdminModeratorAuthorPermission,)

    def get_queryset(self, *args, **kwargs):
        queryset = Comment.objects.all().order_by('id')
        title_id = self.kwargs.get("title_id")
        review_id = self.kwargs.get("review_id")
        title = get_object_or_404(Title, pk=title_id)
        review = get_object_or_404(Review, pk=review_id)
        return queryset.filter(review__title=title, review=review)

    def perform_create(self, serializer, *args, **kwargs):
        review_id = self.kwargs.get("review_id")
        review = get_object_or_404(Review, pk=review_id)
        return serializer.save(
            author=self.request.user,
            review=review
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'username'
    permission_classes = (IsAdmin,)

    @action(methods=['get', 'patch'], detail=False,
            permission_classes=[IsAuthenticated])
    def me(self, request):
        user = get_object_or_404(User, id=request.user.id)
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if request.user.is_admin:
            serializer = UsersSerializer(request.user,
                                         data=request.data,
                                         partial=True)
        else:
            serializer = NotAdminSerializer(request.user,
                                            data=request.data,
                                            partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
