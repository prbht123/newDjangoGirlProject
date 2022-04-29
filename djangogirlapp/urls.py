from django.urls import path,include
from . import views

urlpatterns = [
    path('home/', views.home),
    path('', views.post_list, name='post_list'),
]