from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('bio/', views.bio, name='bio'),
    path('code/', views.code, name='code'),
    path('live/', views.live, name='live'),
    path('build/', views.build, name='build'),
]