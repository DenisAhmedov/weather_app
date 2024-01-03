from django.contrib import admin

from api.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'last_updated', 'temperature', 'wind_speed', 'pressure')
    search_fields = ('name',)
    list_display_links = ('name',)
    ordering = ('name',)

