from django.contrib import admin

from reviews.models import Reviews


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('user', 'review_created_at', 'rating')
    list_display_links = ('user', 'rating')
    list_filter = ('rating',)


admin.site.register(Reviews, ReviewsAdmin)
