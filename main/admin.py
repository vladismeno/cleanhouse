from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'feedback')
    search_fields = ('name', 'feedback')
    list_filter = ('date',)


admin.site.register(Review, ReviewAdmin)