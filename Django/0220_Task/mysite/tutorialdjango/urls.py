from django.contrib import admin
from django.urls import path
from main.views import about, notice, 1, 2, 3, cotact, a, b, c, d, user, hojun, mini

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about),
    path('notice/', notice),
    path('1/', 1),
    path('2/', 2),
    path('3/', 3),
    path('contact/', contact),
    path('a/', a),
    path('b/', b),
    path('c/', c),
    path('d/', d),
    path('user/', user),
    path('hojun/', hojun),
    path('mini/', mini),
]
