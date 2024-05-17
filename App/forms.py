# File: App/forms.py
from django import forms
from .models import Video, Tag, Category


# Form for video upload
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video_file']
