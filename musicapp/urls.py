from django.urls import path, include
from .views import (
    SongListApiView,
    SongDetailApiView
)

urlpatterns = [
    path('song', SongListApiView.as_view()),
    path('song/<int:song_id>/', SongDetailApiView.as_view()),
]
