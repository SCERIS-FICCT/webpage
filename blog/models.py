from django.db import models

from .utils import event_picture_path


# Create your models here.
class EventType(models.Model):
    name = models.CharField(max_length=50)


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    datetime = models.DateTimeField()
    place = models.CharField(max_length=100)
    image = models.ImageField(upload_to=event_picture_path)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)