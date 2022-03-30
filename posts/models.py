from django.conf import settings
from django.db import models


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField()
    title = models.CharField(max_length=256)
    body = models.TextField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=512)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)