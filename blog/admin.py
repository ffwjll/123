from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'likes')
    list_editable = ('likes',)
    save_on_top = True
