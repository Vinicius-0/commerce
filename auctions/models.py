from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField, IntegerField


class User(AbstractUser):
    pass


class Listing(models.Model):
    creator = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    description = models.TextField(max_length=512, default='')
    initialBid = models.FloatField()
    actualBid = models.FloatField(default=0)
    image = models.CharField(max_length=256, null=True)
    isActive = models.BooleanField(default=True)
    dateTime = models.DateTimeField(auto_now_add=True)
    watchers = models.ManyToManyField(
        User, blank=True, related_name='watchedListings')
    winner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title} - {self.category} - {self.isActive} - {self.id} - {self.winner}"


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listingID = models.ForeignKey(Listing, on_delete=models.CASCADE)
    offer = models.FloatField(default="")
    dateTime = models.DateTimeField(auto_now_add=True, null=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=512, default="")
    listingID = models.ForeignKey(Listing, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(auto_now_add=True)
