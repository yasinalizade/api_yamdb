from django.urls import include, path
from rest_framework.routers import DefaultRouter


from .views import CategoryViewSet, CommentViewSet, GenreViewSet
from .views import ReviewViewSet, TitleViewSet

router = DefaultRouter()

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

urlpatterns = [
    path('v1/', include(router.urls), name='api_v1'),
]
