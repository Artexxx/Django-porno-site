from django.shortcuts import render
from videos.models import Video


def get_videos(request):
    template = "main.html"

    videos = Video.objects.all()

    context = {
        "videos": videos,
     }

    return render(request, template, context)


def get_video(request, video_id):
    template = "video.html"

    video = Video.objects.get(id=video_id)

    # Увеличичение количества просмотров
    video.views += 1
    video.save()


    context = {
        "video": video,
    }
    return render(request, template, context)
