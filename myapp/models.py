from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator, ASCIIUsernameValidator
from django.utils import *


# Create your models here.

class Subscribers(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return 'Email:%s,  Name:%s' % (self.email, self.name)

    class Meta:
        verbose_name = 'Sub'
        verbose_name_plural = 'Subs'


class Band(models.Model):
    bands_name = models.CharField(max_length=128)
    email = models.EmailField()
    photo = models.ImageField(null=True, blank=True, default=None, verbose_name='Фото')
    budget = models.CharField(max_length=128)
    user = models.ManyToManyField(User, through='BandUsername', through_fields=('bands_name', 'username'))

    def __str__(self):
        return ' bands_name:%s, Email:%s, budget:%s, photo:%s' % (
            self.bands_name, self.email, self.budget, self.photo)

    def get_artist(self):
        return [{'name': artist.username} for artist in self.user.all()]


class BandUsername(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    bands_name = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return 'username:%s,  bands_name:%s' % (str(self.username.username), str(self.bands_name.bands_name))


class ConcertAgency(models.Model):
    name_CA = models.CharField(max_length=128)
    creation_year = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return 'artist:%s, creation_year:%s, Email:%s' % (self.name_CA, self.creation_year, self.email)


class CA_Band(models.Model):
    name_CA = models.ForeignKey(ConcertAgency)
    bands_name = models.ForeignKey(Band)

    def __str__(self):
        return 'name_CA:%s,  bands_name:%s' % (self.name_CA, self.bands_name)

        # def get_bands(self):
        #     return [{'bands_name': band.bands_name} for band in self.Band.all()]
        #
        # get_bands.short_description = 'Участники'
