from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Post
from .models import PostAdmin
from .models import Category
from .models import Area
from .models import detailArea

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Area)
admin.site.register(detailArea)