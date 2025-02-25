from rest_framework import serializers
from .models import UploadedVideo

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedVideo
        fields = '__all__'
