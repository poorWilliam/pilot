from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class artist(models.Model):
    artist = models.CharField(max_length=50)
    def __str__(self):
        return self.artist

class song(models.Model):
    song=models.CharField(max_length=70)
    artist = models.ForeignKey(
    "artist", on_delete=models.RESTRICT)
    commnent = models.TextField()
    def approve(self):
        self.approved_comment = True
        self.save()
    def __str__(self):
        return self.commnent
    def __str__(self):
        return f'{self.artist} - {self.song}'
