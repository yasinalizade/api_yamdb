from django.urls import include, path
from rest_framework.routers import DefaultRouter

# from .views import CategoryViewSet, CommentViewSet, GenreViewSet
# from .views import ReviewViewSet, TitleViewsSet

router = DefaultRouter()


router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    # ReviewViewSet, ДОБАВИТЬ ПОСЛЕ ОПРЕДЕЛЕНИЯ ВЬЮСЕТА
    basename='review'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    # CommentViewSet, ДОБАВИТЬ ПОСЛЕ ОПРЕДЕЛЕНИЯ ВЬЮСЕТА
    basename='comment'
)

urlpatterns = [
    path('v1/', include(router.urls), name='api_v1'),
]
