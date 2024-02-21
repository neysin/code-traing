from django.urls import path, include
from .views import notice_list, free, oneone

urlpatterns = [
    
    path('', notice_list),
    path('free/', include("free.urls")),
    path('oneone/', include("oneone.urls")),
    
]