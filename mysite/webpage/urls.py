#MyWebPage/mysite/webpage/urls.py
from django.urls import path

from . import views


app_name = 'webpage'


urlpatterns = [
    path("", views.index, name="index"),

]