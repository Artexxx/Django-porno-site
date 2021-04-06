from django.db import models
from django.db.models import Model


class VideoCategory(Model):
    name = models.CharField(max_length=100)





    def __str__(self):
        return self.name











class Video(Model):
    title = models.CharField(verbose_name="Название", max_length=100, default="")
    desc = models.TextField(verbose_name='Описание', max_length=1000, default='', blank=True)
    category = models.ForeignKey(VideoCategory,on_delete=models.SET_NULL,verbose_name='Категория',null=True)
    image = models.FileField(verbose_name="Картика", upload_to="images")
    video = models.FileField(verbose_name="Видео", upload_to="videos")
    author = models.CharField(verbose_name="Автор", max_length=100, default="", blank=True)
    date = models.DateField(verbose_name="Дата", default=None, blank=True, null=True)

    views = models.IntegerField(verbose_name="Количество просмотров", blank=True, default=0)
    likes = models.IntegerField(verbose_name="Количество лайков", blank=True, default=0)
    dislikes = models.IntegerField(verbose_name="Количество дизлайков", blank=True, default=0)


    def __str__(self):
        return self.title
