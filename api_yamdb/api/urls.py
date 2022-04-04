from django.urls import include, path
from rest_framework.routers import DefaultRouter
# from rest_framework.routers import SimpleRouter


from .views import CategoryViewSet, CommentViewSet, GenreViewSet
from .views import ReviewViewSet, TitleViewSet
#  from users.views import send_confirmation_code
from users.views import (APIGetToken, APISignup, UsersViewSet)

router = DefaultRouter()
# router = SimpleRouter()

router.register(
    'categories',
    CategoryViewSet,
    basename='category'
)
router.register(
    'genres',
    GenreViewSet,
    basename='genre'
)
router.register(
    'titles',
    TitleViewSet,
    basename='title'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='review'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

router.register(
    'users',
    UsersViewSet,
    basename='users'
)
urlpatterns = [
    path('v1/auth/token/', APIGetToken.as_view(), name='get_token'),
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
]
