from django.db import models
from django.db.models import Model
from videos.models import Video


class WatchAnalytics(Model):
    sesId = models.CharField(verbose_name="Сессия пользователя", max_length=150, db_index=True)
    videoId = models.ForeignKey(Video, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.sesId)