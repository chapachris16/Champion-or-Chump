from django.contrib import admin

# Register your models here.
from .models import Post, Comments

# Register your models here
admin.site.register(Post)
admin.site.register(Comments)
