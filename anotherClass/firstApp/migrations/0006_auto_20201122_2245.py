# Generated by Django 3.0.4 on 2020-11-22 13:45

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0005_auto_20201122_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='class'),
        ),
    ]
