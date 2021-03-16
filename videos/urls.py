from django.conf.urls import url

from videos.views import get_videos, get_video

urlpatterns = [
    url(r'^main/$', get_videos, name='main'),
    url(r'^id/([0-9]+)/$', get_video, name='main'),

]