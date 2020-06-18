# Generated by Django 3.0.4 on 2020-06-18 07:55

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import firstApp.models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('tutor', models.CharField(max_length=10)),
                ('tutor_photo', imagekit.models.fields.ProcessedImageField(default='', upload_to='tutor')),
                ('tutor_insta', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('tutor_blog', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('tutor_youtube', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('photo', imagekit.models.fields.ProcessedImageField(default='', upload_to='class')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(default='')),
                ('tutor_body', ckeditor_uploader.fields.RichTextUploadingField(default='')),
                ('price', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=5)),
                ('in_min', models.PositiveIntegerField(blank=True, default='1', null=True)),
                ('in_max', models.PositiveIntegerField(blank=True, default='1', null=True)),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('area', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='firstApp.Area')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='firstApp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='firstApp.Category')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=firstApp.models.get_image_filename, verbose_name='Image')),
                ('post', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='firstApp.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('inClass', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='edu_class', to='firstApp.Class')),
                ('state', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='state', to='firstApp.State')),
            ],
        ),
        migrations.CreateModel(
            name='detailArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('parentArea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstApp.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='firstApp.Post')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ClassReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('body', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('inClass', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='review_class', to='firstApp.Class')),
            ],
        ),
        migrations.CreateModel(
            name='ClassQna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('inClass', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='qna_class', to='firstApp.Class')),
            ],
        ),
        migrations.CreateModel(
            name='ClassDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('inClass', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='date_class', to='firstApp.Class')),
            ],
        ),
        migrations.CreateModel(
            name='ClassAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('inClass', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='anw_class', to='firstApp.Class')),
                ('inQuestion', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='answer_class', to='firstApp.ClassQna')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='level', to='firstApp.Level'),
        ),
        migrations.AddField(
            model_name='class',
            name='like_user',
            field=models.ManyToManyField(related_name='like_class', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='class',
            name='mode',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mode', to='firstApp.Mode'),
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('inClass', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='certi_class', to='firstApp.Class')),
            ],
        ),
        migrations.CreateModel(
            name='CComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_comments', to='firstApp.Comment')),
                ('post', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ccomments', to='firstApp.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('number', models.CharField(max_length=13)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(default='')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('date', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='apply', to='firstApp.ClassDate')),
                ('inClass', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='apply', to='firstApp.Class')),
            ],
        ),
    ]
