# blog > urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_list, name="blog"),
    path("<int:pk>/", views.blog_detail, name="post"),
]