from django.urls import path
from dds import views

urlpatterns = [

    path('ddsHome', views.home, name='ddsHome'),
    path('recent/', views.recent, name="recent"),
    path('myfiles/', views.myfiles, name="myfiles"),
    path('trash/', views.trash, name="trash"),
    path('shared/', views.shared, name="shared"),
    path('archive/', views.archive, name="archive"),
    path('publicfolder/', views.publicfolder, name="publicfolder"),
    path('privatefolder/', views.privatefolder, name="privatefolder"),
    path('publicrepo/', views.publicrepo, name="publicrepo"),
    path('privaterepo/', views.privaterepo, name="privaterepo"),
    path('settings/', views.settings, name="settings"),
    path('newgroup/', views.newgroup, name="newgroup"),
    path('help/', views.help, name="help"),

]