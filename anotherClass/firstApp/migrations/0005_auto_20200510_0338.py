# Generated by Django 3.0.5 on 2020-05-09 18:38

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0004_auto_20200510_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=10)),
                ('number', models.CharField(max_length=13)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(default='')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 9, 18, 38, 43, 302242, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 9, 18, 38, 43, 179570, tzinfo=utc)),
        ),
    ]