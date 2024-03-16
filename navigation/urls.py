from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('popular_menu/', views.popular_menu),
]