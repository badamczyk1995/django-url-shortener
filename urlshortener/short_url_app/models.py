from django.db import models
from django.conf import settings


class ShortUrlModel(models.Model):
    long_url = models.CharField(max_length=settings.SHORT_URL_MAX_LENGTH, unique=True)
    short_url = models.CharField(max_length=settings.LONG_URL_MAX_LENGTH, unique=True)

    def __str__(self):
        return f"{self.long_url} in short {self.short_url}"
