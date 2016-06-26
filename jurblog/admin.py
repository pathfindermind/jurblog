from django.contrib import admin

# Register your models here.
from django.contrib import admin
from jurblog.models import NewsEntry
from jurblog.models import Category, NewsEntry

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }

    list_display = ('name', 'slug')


class NewsEntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }

    list_display = ('created_at', 'published_at', 'title', 'draft')
    list_display_links = ('title',)
    list_filter = ('created_at', 'published_at', 'draft')
    date_hierarchy = 'created_at'
    search_fields = ('title', 'tease', 'body')

    exclude = ('created_at',)
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'tease', 'body', 'image')}),
        ('Properties', {'fields': ('draft', 'published_at', 'category')}),
    )
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/django_tinymce/tiny_mce_init.js',
        )


admin.site.register(Category, CategoryAdmin)

admin.site.register(NewsEntry, NewsEntryAdmin)
