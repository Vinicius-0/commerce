from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import DateField, IntegerField


class User(AbstractUser):
    pass


class Listing(models.Model):
    creator = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    description = models.TextField(max_length=512, default='')
    initialBid = models.FloatField()
    actualBid = models.FloatField(null=True)
    image = models.CharField(max_length=256, null=True)
    isActive = models.BooleanField(default=True)
    dateTime = models.DateTimeField(auto_now_add=True)


class Bid(models.Model):
    user = models.CharField(max_length=64, default="")
    title = models.CharField(max_length=64, default="")
    listingID = models.IntegerField(default="")
    bid = models.IntegerField(default="")


class Comment(models.Model):
    user = models.CharField(max_length=64)
    comment = models.CharField(max_length=512, default="")
    listingID = models.IntegerField(default="")
    dateTime = models.DateTimeField(auto_now_add=True)
