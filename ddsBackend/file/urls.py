from django.urls import path
from file import views

urlpatterns = [

    path('upload', views.upload, name='upload'),


    path('archive/<int:pk>/', views.archive, name='archive')

]