from django.urls import path, include
from .views import qna_list, qnadetails

urlpatterns = [
    
    path('', qna_list),
    path('<int:pk>/', qnadetails),
    
]