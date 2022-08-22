from django.contrib import admin
from django.urls import path
from  .import views


urlpatterns = [
   path('',  views.getData, name='routes'),
   path('espdata/', views.getData, name='getdata'),
   path('espdata/data/', views.espData, name='espdata' ),
]