# Generated by Django 3.0.5 on 2020-05-05 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0005_auto_20200505_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]