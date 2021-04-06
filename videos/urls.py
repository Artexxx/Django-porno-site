from django.conf.urls import url

from videos.views import get_videos, get_video, get_videos_sorted_by_rating

urlpatterns = [
    url(r'^rating/$', get_videos_sorted_by_rating, name='rating'),
    url(r'^main/$', get_videos, name='main'),
    url(r'^id/([0-9]+)/$', get_video, name='main'),

]