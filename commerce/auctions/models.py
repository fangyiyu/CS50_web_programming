from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import admin


class User(AbstractUser):
    pass

class Listing(models.Model):
    owner = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=64)
    link = models.CharField(max_length=64,default=None,blank=True,null=True)
    time = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.owner} created a listing of {self.title} at {self.price}"

class Bid(models.Model):
    user = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    listingid = models.IntegerField()
    bid = models.IntegerField()

    def __str__(self):
        return f"{self.title} is bid by {self.user} at {self.bid}"

class Comment(models.Model):
    user = models.CharField(max_length=64)
    time = models.CharField(max_length=64)
    comment = models.TextField()
    listingid = models.IntegerField()
    title = models.CharField(max_length=64, default="foobar")

    def __str__(self):
        return f"{self.user} made a comment on {self.title}: {self.comment}"

class Watchlist(models.Model):
    user = models.CharField(max_length=64)
    listingid = models.IntegerField()
    title = models.CharField(max_length=64, default="foobar")

    def __str__(self):
        return f"{self.user} put {self.title} into watchlist"

class Closedbid(models.Model):
    owner = models.CharField(max_length=64)
    winner = models.CharField(max_length=64)
    listingid = models.IntegerField()
    winprice = models.IntegerField()
    title = models.CharField(max_length=64, default="foobar")

    def __str__(self):
        return f"{self.title} is bought by {self.winner} at price {self.winprice}"

class Alllisting(models.Model):
    listingid = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.TextField()
    link = models.CharField(max_length=64,default=None,blank=True,null=True)

    def __str__(self):
        return f"{self.title}"
