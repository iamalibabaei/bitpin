from django.contrib import admin

from .models import Post, PostScore


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(PostScore)
class PostScoreAdmin(admin.ModelAdmin):
    pass
