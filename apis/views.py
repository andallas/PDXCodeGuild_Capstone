from urllib import response
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from posts import models as postModels
from .serializers import PostSerializer, CommentSerializer
from datetime import datetime


class PostViewSet(viewsets.ModelViewSet):
    currentDate = datetime.now()
    queryset = postModels.Post.objects.filter(published_at__lt=currentDate)
    serializer_class = PostSerializer

    @action(detail=True, methods=['put', 'get'])
    def vote(self, request, pk=None):
        post = self.get_object()
        
        if (request.method == 'PUT'):
            post.votes += 1
            post.save()
            responseObject = {'vote': 'Success', 'voteCount': f'{post.votes}'}
        elif (request.method == 'GET'):
            responseObject = {'vote': 'Failure', 'voteCount': f'{post.votes}'}
        else:
            responseObject = {'vote': 'Failure', 'errorMessage': f'Invalid request type: {request.method}'}

        return Response(responseObject)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = postModels.Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]