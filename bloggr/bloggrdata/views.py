from rest_framework import generics

from .models import Post
from .serializers import PostSerializer



class PostList(generics.ListCreateAPIView):
    model = Post
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Post
    serializer_class = PostSerializer