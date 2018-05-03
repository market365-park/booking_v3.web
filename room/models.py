from django.conf import settings
from django.db import models

class RoomBooking(models.Model):
    title = models.CharField('TITLE', max_length=50)
    room_id = models.CharField('ROOM', max_length=50, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, auto_created=True, on_delete=models.CASCADE)
    start_time = models.DateTimeField('Start Time')
    end_time = models.DateTimeField('End Time')
    create_time = models.DateTimeField('Create Time', auto_now_add=True)

    class Meta:
        verbose_name = 'room_booking'
        verbose_name_plural = 'room_bookings'
        ordering = ('-start_time',)

    def __str__(self):
        return self.title

class Room(models.Model):
    room_id = models.CharField('ROOM_ID', max_length=50)
    room_name = models.CharField('ROOM_NAME', max_length=50)
    event_color = models.CharField('COLOR', max_length=50)

    class Meta:
        verbose_name = 'room'
        verbose_name_plural = 'rooms'

    def __str__(self):
        return self.room_id
