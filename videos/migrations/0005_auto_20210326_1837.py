# Generated by Django 3.1 on 2021-03-26 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_auto_20210319_1753'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='opisanie',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='watched_like',
            new_name='likes',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='watched_count',
            new_name='views',
        ),
    ]
