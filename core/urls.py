from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro-teste/', views.registro_teste, name='registro_teste'),
]