# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.db import models

# Create your models here.

from django.db import models
class File(models.Model):
  file = models.FileField(blank=False, null=False)
  gender = models.BooleanField(default=False)
  age = models.IntegerField(default=0, null=False)
  timestamp = models.DateTimeField(auto_now_add=True)