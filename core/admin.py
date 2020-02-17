from django.contrib import admin
from .models import Item


class SnippetAdmin(admin.ModelAdmin):
    list_filter = ('created',)
    list_display = ['title', 'created']


admin.site.site_header = 'Marko Admin Dashboard'
admin.site.register(Item)
