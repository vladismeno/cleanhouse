from django.contrib import admin
from .models import Review
from django.utils.safestring import mark_safe


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'feedback', 'image_preview')
    search_fields = ('name', 'feedback')
    list_filter = ('date',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50"/>')
        return ''


admin.site.register(Review, ReviewAdmin)