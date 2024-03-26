from django.contrib import admin
from .models import PerformanceItem

@admin.register(PerformanceItem)
class PerformanceItemAdmin(admin.ModelAdmin):
    # list_display = ['identifier', 'url']
    pass