from django.db import models

class Image(models.Model):
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pictures/%Y/%m/%d/', max_length=255, blank=True)

class XPTO(models.Model):
    description=models.CharField(max_length=50)

    def __str__(self):
        return self.description
    