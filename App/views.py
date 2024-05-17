# File: App/views.py
import requests
from decouple import config
from django.shortcuts import render
from App.forms import VideoForm
from App.models import Tag, Category, Video


# View to handle video upload from the video upload form
def upload_video(request):
    form = VideoForm()
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the video
            form.save()
            # Process the video file with the worker
            video_url = config("DOMAIN") + form.instance.video_file.url
            worker_url = config("WORKER_URL") + "/process_video?video_url=" + video_url
            # Send a GET request to the worker URL
            response = requests.get(worker_url)
            if response.status_code == 200:
                # Get the response data
                response_data = response.json()
                # Save the video tags
                tags = response_data.get('tags')
                for tag in tags:
                    tag, created = Tag.objects.get_or_create(name=tag)
                    form.instance.tags.add(tag)
                # Save the video categories
                categories = response_data.get('categories')
                for category in categories:
                    category, created = Category.objects.get_or_create(name=category)
                    form.instance.categories.add(category)
                # Save the video duration and resolution
                form.instance.duration = response_data.get('duration')
                form.instance.size = response_data.get('resolution')
                form.instance.save()
            # Return a success message
            return render(request, 'upload_video.html',
                          {'form': form, 'message': 'Video uploaded successfully!'})
        else:
            # Return the form with errors
            return render(request, 'upload_video.html', {'form': form,
                                                         'message': 'Error uploading video!'})
    return render(request, 'upload_video.html', {'form': form})


def list_videos(request):
    videos = Video.objects.all()
    return render(request, 'list_videos.html', {'videos': videos})
