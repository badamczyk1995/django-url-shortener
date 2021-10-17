from random import choice
from string import ascii_letters, digits
from django.conf import settings
from .models import ShortUrlModel


class Generate:
    def __init__(self):
        self.chars = ascii_letters + digits
        self.length = settings.RANDOM_URL_STRING_LENGTH
        self.model = ShortUrlModel

    def random_string(self):
        return ''.join([choice(self.chars) for _ in range(self.length)])

    def short_url(self):
        random_string = self.random_string()
        if self.model.objects.filter(short_url=random_string).exists():
            return self.short_url()
        return random_string
