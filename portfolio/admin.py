from django.contrib import admin
from .models import Category , PortfolioImage, PortfolioProject

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 3
    fields = ('image', 'caption', 'order')




@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'event_date',
        'is_featured',
        'is_published',
        'created_at'
    )
    list_editable = ('is_featured', 'is_published')
    list_filter = ('category', 'is_featured', 'is_published', 'event_date')
    search_fields = ('title', 'description', 'location')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'event_date'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('category', 'title', 'slug')
        }),
        ('المحتوى', {
            'fields': ('description', 'cover_image', 'video_clip')
        }),
        ('التفاصيل', {
            'fields': ('event_date', 'location', 'is_featured', 'is_published')
        }),
        ('البيانات الوصفية', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    inlines = [PortfolioImageInline]
