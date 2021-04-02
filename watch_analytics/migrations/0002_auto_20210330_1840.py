# Generated by Django 3.1 on 2021-03-30 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20210326_1837'),
        ('watch_analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchanalytics',
            name='session_key',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Сессия пользователя'),
        ),
        migrations.AlterField(
            model_name='watchanalytics',
            name='video_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='videos.video'),
        ),
    ]