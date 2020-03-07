from django.urls import path

from . import views

app_name = 'log'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /coffee/1/
    path('coffee/<int:coffee>/', views.coffee_detail, name='detail'),
    # ex: /coffee/1/roasts/
    path('coffee/<int:coffee>/roasts/', views.roasts, name='roasts'),
]