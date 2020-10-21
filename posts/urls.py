from django.urls import path

from posts.views import PostAPIView, PostDetailAPIView

urlpatterns = [
    path('<int:pk>', PostDetailAPIView.as_view()),
    path('',PostAPIView.as_view()),
    ]
