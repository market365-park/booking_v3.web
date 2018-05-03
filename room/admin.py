from django.contrib import admin
from .models import RoomBooking, Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'room_name', 'event_color')


class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'room_id', 'owner', 'create_time')
    search_fields = ('title',)
    list_filter = ('room_id',)
    ordering = ('-start_time', 'room_id',)


admin.site.register(Room, RoomAdmin)
admin.site.register(RoomBooking, RoomBookingAdmin)
