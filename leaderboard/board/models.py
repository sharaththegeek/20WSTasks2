# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=20)

class UserProfile(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    email=models.OneToOneField(User)
    points=models.IntegerField()
