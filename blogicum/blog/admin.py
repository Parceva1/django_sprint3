from django.contrib import admin

from .models import Category, Post, Location

admin.site.empty_value_display = 'Не задано'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug',
                    'is_published', 'created_at')
    list_per_page = 10
    list_editable = ('description', 'is_published')
    list_display_links = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category',
                    'location', 'pub_date', 'is_published', 'created_at')
    list_filter = ('category', 'location', 'is_published', 'pub_date')
    search_fields = ('title', 'text')
    list_per_page = 10


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Location)
