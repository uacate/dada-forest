from django.contrib import admin
from .models import URLSource

@admin.register(URLSource)
class URLSourceAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'url']

# admin.site.register(URLSource)