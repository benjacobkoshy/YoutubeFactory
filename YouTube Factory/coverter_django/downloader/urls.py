from django.urls import path
from .views import download_video, download_audio

urlpatterns = [
    path('download/video/', download_video, name='download_video'),
    path('download/audio/',download_audio,name="download_audio"),
    
]
