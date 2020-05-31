from django.urls import path
from . import views

app_name = 'matcher'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.usr_login, name='usr_login'),
]