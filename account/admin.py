from django.contrib import admin
from account.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone', 'email')
    search_fields = ('first_name',)
    list_filter = ('last_name',)
    ordering = ('first_name', 'last_name', 'username',)

admin.site.register(User, UserAdmin)

