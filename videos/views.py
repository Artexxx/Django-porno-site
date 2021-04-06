from django.shortcuts import render
from videos.models import Video, VideoCategory
from watch_analytics.models import  WatchAnalytics


def get_videos(request):
    template, context = get_template_context()

    return render(request, template, context)

def get_videos_sorted_by_rating(request):
    template, context = get_template_context()
    videos = context["videos"]
    context["videos"] = videos.order_by('-rating')
    return render(request, template, context)


def get_template_context():
    template = "main.html"

    videos = Video.objects.all()
    categories = VideoCategory.objects.all()

    context = {
        "videos": videos,
        "categories": categories,
    }
    return template, context

def get_video(request, video_id):
    template = "video.html"

    video = Video.objects.get(id=video_id)

    if not request.session.session_key:
        request.session.save()

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
