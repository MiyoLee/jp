# Generated by Django 3.0.5 on 2020-05-05 16:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0007_auto_20200505_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 5, 16, 13, 18, 874380, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 5, 16, 13, 18, 802366, tzinfo=utc)),
        ),
    ]
