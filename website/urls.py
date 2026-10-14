#НАСТРОЙКА МАРШРУТИЗАЦИИ
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('oferta/', views.oferta, name='oferta'),
    path('privacy/', views.privacy, name='privacy'),
]
