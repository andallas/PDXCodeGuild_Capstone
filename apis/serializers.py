from rest_framework import serializers
from accounts import models as accountModels
from posts import models as postModels
from games import models as gameModels


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'bio_text',
            'user',
        )
        model = accountModels.UserInfo

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'created_at',
            'updated_at',
            'published_at',
            'title',
            'body',
            'author',
            'votes',
        )
        model = postModels.Post

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'created_at',
            'updated_at',
            'post',
            'body',
            'author',
        )
        model = postModels.Comment

class GameInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'created_at',
            'name',
            'description',
        )
        model = gameModels.GameInfo

class GameScoreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'created_at',
            'score',
            'game',
            'user',
        )
        model = gameModels.GameScore

class GameAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'created_at',
            'name',
            'description',
            'game',
            'user',
        )
        model = gameModels.GameAchievement
