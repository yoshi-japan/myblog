# Generated by Django 2.2.5 on 2020-03-07 14:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200307_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='creat_data',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 7, 14, 34, 8, 756575, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='created_data',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 7, 14, 34, 8, 755546, tzinfo=utc)),
        ),
    ]
