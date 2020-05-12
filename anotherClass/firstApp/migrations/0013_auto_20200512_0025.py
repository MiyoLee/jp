# Generated by Django 3.0.5 on 2020-05-11 15:25

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0012_auto_20200512_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='classtitle',
        ),
        migrations.AddField(
            model_name='apply',
            name='inClass',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='apply_class', to='firstApp.Class'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 11, 15, 25, 43, 754924, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 11, 15, 25, 43, 635245, tzinfo=utc)),
        ),
    ]
