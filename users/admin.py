from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_of_birth', 'get_photo')
    list_display_links = ('id', 'user')
    search_fields = ('date_of_birth', 'user__username')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{ obj.photo.url }" width="75px"')
        return '-'

    get_photo.short_description = 'Фото'


admin.site.register(Profile, ProfileAdmin)
