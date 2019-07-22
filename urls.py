Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
