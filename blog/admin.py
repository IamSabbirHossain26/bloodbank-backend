from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}  # auto slug from title
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'created_at')
