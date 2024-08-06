from django.db import models

# Create your models here.

from django.db import models


class TgUser(models.Model):
    telegram_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    location_lat = models.CharField(max_length=100, null=True, blank=True)
    location_long = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    user = models.ForeignKey(TgUser, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text
