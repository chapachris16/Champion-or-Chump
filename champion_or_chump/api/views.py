from django.shortcuts import render
from rest_framework import generics
from .models import Post, Comments
from .serializers import PostSerializer, CommentsSerializer
# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pass

class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pass

