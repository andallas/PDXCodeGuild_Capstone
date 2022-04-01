from django.urls import path
from .views import PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register('post', PostViewSet, basename='posts')
router.register('comment', CommentViewSet, basename='comments')
urlpatterns = router.urls