from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path ('',views.api_views.as_view()),
    path ('<int:pk>/',views.api_views.as_view())
]