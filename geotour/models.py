import datetime
from django.db import models
from django.utils import timezone
import datetime

class Transport(models.Model):
    transportType = models.CharField(max_length=200)
    def __unicode__(self):
        return self.transportType

class Area(models.Model):
    interestType = models.CharField(max_length=200)
    def __unicode__(self):
        return self.interestType

class Tour(models.Model):
    name = models.CharField(max_length=200)
    fromAddress = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    returnAddress = models.CharField(max_length=200)
    startTime = models.DateTimeField(default=timezone.now())
    endTime = models.DateTimeField(default=datetime.date.today())
    transport = models.ManyToManyField(Transport)
    areas =  models.ManyToManyField(Area)
    def __unicode__(self):
        return self.name   

class Place(models.Model):
    tour = models.ForeignKey(Tour)
    name = models.CharField(max_length=200)
    time = models.DateTimeField(default=datetime.date.today())
    address = models.CharField(max_length=200)
    details =  models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ('address',)

class Area(models.Model):
    interestType = models.CharField(max_length=200)	


# amusement_park
# aquarium
# art_gallery
# zoo
# movie_theater
# museum
# bowling_alley


# food
# bakery
# cafe
# restaurant
# bar
# night_clubpark


# shopping_mall
# book_store
# clothing_store
# department_store
# jewelry_store
# spa
