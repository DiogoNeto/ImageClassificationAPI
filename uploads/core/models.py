from __future__ import unicode_literals

from django.db import models

GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

# attributes to classify the input image
class Document(models.Model):
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    age = models.IntegerField(max_length=3)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
