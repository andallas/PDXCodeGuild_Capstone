from .views import PostViewSet, CommentViewSet, UserInfoViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('post', PostViewSet, basename='posts')
router.register('comment', CommentViewSet, basename='comments')
router.register('userInfo', UserInfoViewSet, basename='userInfo')
urlpatterns = router.urls