# Generated by Django 3.0.5 on 2020-05-27 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0003_auto_20200528_0404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]