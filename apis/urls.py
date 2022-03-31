from django.urls import path
from .views import PostViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register('post', PostViewSet, basename='posts')
urlpatterns = router.urls