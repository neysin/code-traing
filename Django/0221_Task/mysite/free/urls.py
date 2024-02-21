from django.urls import path, include
from .views import free_list, freedetails

urlpatterns = [
    
    path('', free_list),
    path('<int:pk>', freedetails),
    
]