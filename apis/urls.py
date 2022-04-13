from .views import PostViewSet, CommentViewSet, UserInfoViewSet, GameInfoViewSet, GameScoreViewSet, GameAchievementViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('post', PostViewSet, basename='posts')
router.register('comment', CommentViewSet, basename='comments')
router.register('userInfo', UserInfoViewSet, basename='userInfo')
router.register('gameInfo', GameInfoViewSet, basename='gameInfo')
router.register('gameScore', GameScoreViewSet, basename='gameScore')
router.register('gameAchievement', GameAchievementViewSet, basename='gameAchievement')
urlpatterns = router.urls