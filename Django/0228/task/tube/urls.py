from django.urls import path
from . import views

urlpatterns = [
    path("", views.tube_list, name ='tube_list'),
    path("<int:pk>", views.tube_detail, name ='tube_detail'),
    path("create/", views.tube_create, name ='tube_create'),
    path("update/<int:pk>/", views.tube_update, name ='tube_update'),
    path("delete/<int:pk>/", views.tube_delete, name ='tube_delete'),
]
