from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', index),
    path('', include(main.urls)),
    path('blog', include(blog.urls)),
]
