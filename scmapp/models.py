from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=40)
    gender = models.CharField(max_length=6)
    password = models.CharField(max_length=20)

class Admin(models.Model):
    aid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

class Event(models.Model):
    eid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    date = models.DateField(settings.DATE_FORMAT)
    time = models.TimeField()
    duration = models.IntegerField()

class Book_ground(models.Model):
    bid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    name = models.CharField(max_length=20)
    date = models.DateField(settings.DATE_FORMAT)
    time = models.TimeField()
    mobile = models.CharField(max_length=10)

class Admission(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    numbers = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)
