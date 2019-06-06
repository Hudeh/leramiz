from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published")
    list_display_links = ("id", "title")
    list_filter = ("title", "realtor")
    list_editable = ("is_published",)
    search_fields = ("title", "realtor")
    list_per_page = 25

admin.site.register(Blog, BlogAdmin)

# Register your models here.