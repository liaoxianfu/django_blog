from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'created_time',
        'modified_time',
        'author',
    ]


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
