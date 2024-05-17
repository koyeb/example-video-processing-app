# File: App/models.py
from django.db import models


# Model to store video metadata
class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    duration = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    size = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.title


# Model to store video related tags
class Tag(models.Model):
    name = models.CharField(max_length=50)
    video = models.ManyToManyField(Video, related_name='tags')

    def __str__(self):
        return self.name


# Model to store video classification
class Category(models.Model):
    name = models.CharField(max_length=50)
    video = models.ManyToManyField(Video, related_name='categories')

    def __str__(self):
        return self.name
