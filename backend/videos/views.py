from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import UploadedVideo
from .serializers import VideoSerializer
from .detection import detect_accidents
from .clip_extraction import extract_clip
import os

@api_view(['POST'])
def upload_video(request):
    if 'video' not in request.FILES:
        return Response({'error': 'No video file provided'}, status=400)

    video_file = request.FILES['video']
    
    # Save video file and get absolute path
    video_path = default_storage.save(f"videos/{video_file.name}", ContentFile(video_file.read()))
    video_absolute_path = default_storage.path(video_path)

    # Save video instance
    video_instance = UploadedVideo.objects.create(video=video_path)

    try:
        # Run accident detection
        detection_results = detect_accidents(video_absolute_path)
    except Exception as e:
        print(f"Error in detect_accidents: {str(e)}")
        return Response({'error': 'Accident detection failed', 'details': str(e)}, status=500)

    # If accident detected, extract the clip
    if detection_results:
        clip_path = f"clips/{video_file.name}"  # Relative path
        clip_absolute_path = os.path.join("media", clip_path)  # Full path

        try:
            extract_clip(video_absolute_path, start_time=5, duration=10, output_path=clip_absolute_path)
            video_instance.clip_path = clip_path  # Save only the relative path
            video_instance.processed = True
            video_instance.save()
            return Response({'message': 'Accident detected', 'clip_path': video_instance.clip_path})
        except Exception as e:
            print(f"Error in extract_clip: {str(e)}")
            return Response({'error': 'Clip extraction failed', 'details': str(e)}, status=500)

    return Response({'message': 'No accident detected'})
