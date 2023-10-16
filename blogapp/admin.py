from django.contrib import admin
from .models import Category1,Category2,Post
# Register your models here.

admin.site.register(Post)
admin.site.register(Category1)
admin.site.register(Category2)
