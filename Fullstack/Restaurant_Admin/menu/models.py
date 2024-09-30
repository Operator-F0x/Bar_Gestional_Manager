from pyexpat import model
from django.db import models

class menucold(models.Model):
   img = models.ImageField()
   title = models.CharField(max_length=30)
   description = models.CharField(max_length=120)
   price =  models.FloatField()

   def __str__(self) -> str:
        return self.title

class menuhot(models.Model):
   img = models.ImageField()
   title = models.CharField(max_length=30)
   description = models.CharField(max_length=120)
   price =  models.FloatField()

   def __str__(self) -> str:
        return self.title

class juice(models.Model):
   img = models.ImageField()
   title = models.CharField(max_length=30)
   description = models.CharField(max_length=120)
   price =  models.FloatField()

   def __str__(self) -> str:
        return self.title


class special(models.Model):
   img = models.ImageField()
   title = models.CharField(max_length=30)
   description = models.CharField(max_length=120)

   def __str__(self) -> str:
        return self.title