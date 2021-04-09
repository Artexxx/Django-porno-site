from django.contrib import admin
from videos.models import Video, VideoCategory

admin.site.register(Video)
admin.site.register(VideoCategory)