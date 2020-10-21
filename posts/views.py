from rest_framework import generics, permissions

from core.models import Post
from posts.serializers import PostSerializer, PostDetailSerializer
from posts.permissions import IsAuthorOrReadOnly

class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
