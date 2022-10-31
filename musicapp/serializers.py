from django.db.models import fields
from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Song
        fields = ['title', 'date_released', 'likes']