from django.db import models

class UploadedVideo(models.Model):
    video = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    clip_path = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Video {self.id} - Processed: {self.processed}"
