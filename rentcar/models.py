from django.db import models
from django.conf import settings


class Car(models.Model):
    class LanguageTypes(models.TextChoices):
        UZBEK = 'uzbek', 'Uzbek'
        RUSSIAN = 'russian', 'Russian'
        ENGLISH = 'english', 'English'

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    car_type = models.TextField()
    color = models.TextField()
    made_year = models.PositiveIntegerField(null=True)
    description = models.TextField()
    price = models.IntegerField()
    motor = models.TextField()
    image = models.ImageField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='rentcar')
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, related_name='rentcar')


class Category(models.Model):
    name = models.CharField(max_length=50)


class Owner(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)


class PayRent(models.Model):
    card = models.CharField(max_length=16)
    expire = models.CharField(max_length=5)
