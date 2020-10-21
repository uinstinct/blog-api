from rest_framework import generics

from core.models import Post
from posts.serializers import PostSerializer

class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
