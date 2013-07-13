from django.db import models
from django.utils import timezone
import datetime

class Transport(models.Model):
    transportType = models.CharField(max_length=200)

class Area(models.Model):
    interestType = models.CharField(max_length=200)

class Tour(models.Model):
	name = models.CharField(max_length=200)
	fromAddress = models.CharField(max_length=200)
	destination = models.CharField(max_length=200)
	returnAddress = models.CharField(max_length=200)
	startTime = models.DateTimeField(default=timezone.now())
	endTime = models.DateTimeField(default=datetime.date.today())
	transport = models.ManyToManyField(Transport)
	areas =  models.ManyToManyField(Area)	

class Place(models.Model):
	tour = models.ForeignKey(Tour)
	name = models.CharField(max_length=200)
	time = models.DateTimeField(default=datetime.date.today())
	address = models.CharField(max_length=200)
	details =  models.CharField(max_length=200)

