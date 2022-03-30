from rest_framework import serializers
from accounts import models
from posts import models
from games import models


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'bio_text',
            'user',
        )
        model = models.UserInfo

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
        model = models.Post

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
        model = models.Comment

class GameInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'created_at',
            'name',
            'description',
        )
        model = models.GameInfo

class GameScoreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'created_at',
            'score',
            'game',
            'user',
        )
        model = models.GameScore

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
        model = models.GameAchievement
