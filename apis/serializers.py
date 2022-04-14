from rest_framework import serializers
from accounts import models as accountModels
from posts import models as postModels
from games import models as gameModels


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'username',
            'email'
        )
        model = accountModels.CustomUser

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'bio_text',
            'user',
        )
        model = accountModels.UserInfo

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField(source="author.username")
    class Meta:
        fields = (
            'id',
            'created_at',
            'updated_at',
            'published_at',
            'title',
            'body',
            'author',
            'author_name',
            'votes',
        )
        model = postModels.Post

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField(source="author.username")
    class Meta:
        fields = (
            'id',
            'created_at',
            'updated_at',
            'post',
            'body',
            'author',
            'author_name',
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
    game_title = serializers.StringRelatedField(source="game.name")
    class Meta:
        fields = (
            'id',
            'created_at',
            'score',
            'game',
            'game_title',
            'user',
        )
        model = gameModels.GameScore

class GameAchievementSerializer(serializers.ModelSerializer):
    game_title = serializers.StringRelatedField(source="game.name")
    class Meta:
        fields = (
            'id',
            'created_at',
            'name',
            'description',
            'game',
            'game_title',
            'user',
        )
        model = gameModels.GameAchievement
        
