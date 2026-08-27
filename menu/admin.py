from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse

from .models import Category, HomepageImage, MenuItem, SiteSettings


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured')
    search_fields = ('name', 'description')
    list_editable = ('is_featured',)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    """Singleton admin: always edits the one SiteSettings row, no add/delete."""

    fields = (
        'restaurant_name', 'logo', 'intro_text',
        'address', 'phone', 'email', 'opening_hours',
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = SiteSettings.load()
        return redirect(reverse('admin:menu_sitesettings_change', args=[obj.pk]))


@admin.register(HomepageImage)
class HomepageImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image', 'order')
    list_editable = ('order',)
    ordering = ('order', 'id')
