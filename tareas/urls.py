from django.urls import path
from .views import index, register
from . import views

urlpatterns = [
    path('index/', index, name='index'),
    path('register/', register, name='register'),
    path('', views.index, name='tareas'),
]