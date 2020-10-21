from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), # useful for adding authorization in rest_framework
]
