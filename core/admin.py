from django.contrib import admin
from .models import PhotographerProfile, Service

@admin.register(PhotographerProfile)
class PhotographerProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'phone', 'location')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ( 'title','order', 'is_active')
    list_editable = ('order','is_active')
    list_filter = ('is_active',)
    search_fields = ('title','description')