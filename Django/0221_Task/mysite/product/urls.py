from django.urls import path, include
from .views import product_list, productdetails

urlpatterns = [
    
    path('', product_list),
    path('<int:pk>/', productdetails),
    
]