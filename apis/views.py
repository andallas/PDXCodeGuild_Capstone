from django.shortcuts import get_object_or_404
from rest_framework import status


from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from posts import models as postModels
from accounts import models as accountModels
from .serializers import CustomUserSerializer, PostSerializer, CommentSerializer, UserInfoSerializer
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
        else:
            responseObject = {'vote': 'Failure', 'errorMessage': f'Invalid request type: {request.method}'}

        return Response(responseObject)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_query_params = self.request.query_params.getlist("post")
        if (len(post_query_params)):
            post_id = post_query_params[0]
            queryset = postModels.Comment.objects.filter(post=post_id)
        else:
            queryset = postModels.Comment.objects.all()
        return queryset

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = accountModels.UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['get'], detail=False, url_path='username/(?P<username>\w+)')
    def getByUsername(self, request, username):
        user = get_object_or_404(accountModels.CustomUser, username=username)
        user_data = CustomUserSerializer(user).data
        userInfo = get_object_or_404(accountModels.UserInfo, user=user_data['id'])
        userInfo_data = UserInfoSerializer(userInfo).data
        return Response(userInfo_data, status=status.HTTP_200_OK)

