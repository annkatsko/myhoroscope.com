from django.conf import settings
from django.db import models
from Vape.choices import SIGNS


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    telegram = models.CharField('Ник в Telegram', max_length=50, blank=True)
    zodiac_sign = models.CharField('Знак зодиака', max_length=50, blank=True, choices=SIGNS)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
