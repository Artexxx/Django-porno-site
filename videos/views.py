from django.shortcuts import render
from videos.models import Video
from watch_analytics.models import  WatchAnalytics


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

    if not request.session.session_key:
        request.session.save()

    print("request.session.session_key:",
          request.session.session_key)

    # получаем сессию
    session_key = request.session.session_key

    is_views = WatchAnalytics.objects.filter(videoId=video_id, sesId=session_key)

    # если нет информации о просмотрах создаем ее
    if is_views.count() == 0 and str(session_key) != 'None':
        views = WatchAnalytics()
        views.sesId = session_key
        views.videoId = video
        views.save()

        # Увеличичение количества просмотров
        video.views += 1
        video.save()


    context = {
        "video": video,
    }
    return render(request, template, context)
