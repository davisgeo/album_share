from django.db import models

from django.contrib.auth.models import User, Group


# Create your models here.

class Album(models.Model):
    album_name = models.CharField(max_length=100, default='')
    created_date = models.DateTimeField(blank=True, null=True, auto_now=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    private = models.BooleanField(default=False)
    cover_photo_id = models.IntegerField(blank=True, null=True)


class Photo(models.Model):
    title = models.CharField(max_length=100, default='')
    uploaded_date = models.DateTimeField(blank=True, null=True, auto_now=True)
    private = models.BooleanField(default=False)
    album_cover = models.BooleanField(default=False)
    album = models.ForeignKey(Album, blank=True, null=True, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos', null=True, blank=True)
