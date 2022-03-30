from django.contrib import admin
from .models import GameInfo, GameScore, GameAchievement


admin.site.register(GameInfo)
admin.site.register(GameScore)
admin.site.register(GameAchievement)
