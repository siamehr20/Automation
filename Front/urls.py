from django.urls import path
from . import views


urlpatterns = [
    path('title', views.show_title),
    path('',),
]
