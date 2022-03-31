from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from posts import models as postModels
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = postModels.Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAdminUser,)

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        post = self.get_object()
        post.votes += 1
        post.save()
        
        return Response({'vote': 'Success', 'voteCount': f'{post.votes}'})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = postModels.Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAdminUser,)