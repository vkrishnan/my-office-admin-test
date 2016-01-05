from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

REGION_CHOICES = (
    (10, 'INDIA'),
    (20, 'SOUTH INDIA'),
    (30, 'KARNATAKA'),
    (40, 'BANGALORE'),
    (50, 'SOUTH BANGALORE'),
    (60, 'HSR LAYOUT'))

'''
class Customer(models.Model):
    #name = models.CharField(max_length=200)
    user = models.OneToOneField(User)
    #contact_person = models.CharField(max_length=100)
    contact_number = PhoneNumberField(unique=True)
    address = models.TextField(max_length=500)
    
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
'''
 
class Order(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    order_date = models.DateTimeField()
    #price = models.FloatField()
    #payment = models.FloatField()
    
class Vendor(models.Model):
    name = models.CharField(max_length=200)
    area_served = models.IntegerField(choices=REGION_CHOICES, default='BANGALORE')
    contact_person = models.CharField(max_length=100)
    contact_number = PhoneNumberField(unique=True)
    address = models.TextField(max_length=500)
    
class Transaction(models.Model):
    order = models.ForeignKey(Order)
    vendor = models.OneToOneField(Vendor)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.FloatField()
    payment = models.FloatField()
    comments = models.TextField(max_length=500)
    
