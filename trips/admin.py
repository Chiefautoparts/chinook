from django.contrib import admin
from .models import River
# Register your models here.

class RiverAdmin(admin.ModelAdmin):
	list_display = ('name', 'location', 'itinerary', 'duration', 'difficulty')

admin.site.register(River, RiverAdmin)