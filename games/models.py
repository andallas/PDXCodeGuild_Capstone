from django.conf import settings
from django.db import models


class GameInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

class GameScore(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)
    game = models.ForeignKey(GameInfo, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class GameAchievement(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    game = models.ForeignKey(GameInfo, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
