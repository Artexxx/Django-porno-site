from django.db import models
from django.db.models import Model


class Video(Model):
    name = models.CharField(max_length=100, default="", verbose_name="Название")
    image = models.FileField(verbose_name="Картика", upload_to="images")
    video = models.FileField(verbose_name="Видео", upload_to="videos")

    author = models.CharField(max_length=100, default="", blank=True, verbose_name="Автор")
    date = models.DateField(verbose_name="Дата", default=None, blank=True, null=True)
    watched_count = models.IntegerField(verbose_name="Количество просмотров", blank=True, default=0)

    def __str__(self):
        return self.name