from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone', 'email')
    search_fields = ('first_name',)
    list_filter = ('last_name',)
    ordering = ('first_name', 'last_name', 'username',)

#class LDAPUserAdmin(admin.ModelAdmin):
#    exclude = ['dn', 'objectClass']
#    list_display = ['first_name','last_name', 'username']
#    search_fields = ('first_name',)
#    list_filter = ('last_name',)
#    ordering = ('first_name', 'last_name', 'username',)


admin.site.register(User, UserAdmin)
#admin.site.register(LdapUser, LDAPUserAdmin)

