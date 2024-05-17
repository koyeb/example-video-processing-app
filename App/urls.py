# File: App/urls.py
from django.urls import path
from App import views


urlpatterns = [
    path('', views.list_videos, name='list_videos'),
    path('upload', views.upload_video, name='upload_video'),
]
