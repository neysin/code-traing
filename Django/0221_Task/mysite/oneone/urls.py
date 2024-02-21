from django.urls import path, include
from .views import oneone_list, oneonedetails

urlpatterns = [
    
    path('', oneone_list),
    path('<int:pk>', oneonedetails),
    
    
]