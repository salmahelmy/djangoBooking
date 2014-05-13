from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.hotel_name
    
class Branch(models.Model):
    branch_name = models.CharField(max_length=100)
    
