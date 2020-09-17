from django.db import models


class supplier(models.Model):
    Address = models.CharField(max_length=100,null=True)    
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    country = models.CharField(max_length=100,null=True)
    Pincode = models.CharField(max_length=100,null=True)

