from django.contrib import admin
from .models import URLSource

@admin.register(URLSource)
class URLSourceAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'title', 'url', 'created_on', 'updated_on']
