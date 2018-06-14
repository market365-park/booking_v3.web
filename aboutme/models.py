from django.conf import settings
from django.db import models

class Biography(models.Model):
    nickname = models.CharField('NICKNAME', max_length=50, blank=True)
    likey = models.CharField('LIKEY', max_length=50, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, auto_created=True, on_delete=models.CASCADE, unique=True)
    profile_pic = models.ImageField('PROFILE_PICTURE', null=True, upload_to='profile_pic', default='profile_pic/anonymous.png')
    backgound_pic = models.ImageField('BACKGROUND_PICTURE', null=True, upload_to='background_pic', default='background_pic/default.png')

    class Meta:
        ordering = ('')

    def __str__(self):
        return self.nickname


