from django.contrib import admin
from django.utils.safestring import mark_safe

from news.models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_news', 'category', 'created_at', 'updated_at', 'get_photo_news')
    list_display_links = ('id', 'title_news')
    search_fields = ('title_news', 'updated_at')
    list_filter = ('category', )

    def get_photo_news(self, obj):
        if obj.photo_news:
            return mark_safe(f'<img src="{ obj.photo_news.url }" width="75px"')
        return '-'

    get_photo_news.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
