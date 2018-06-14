from django.contrib import admin
from .models import *


class BiographyAdmin(admin.ModelAdmin):
	list_display = ('nickname', 'likey', 'owner')

admin.site.register(Biography, BiographyAdmin)
	
