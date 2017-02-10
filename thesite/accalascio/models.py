from tinymce.models import HTMLField
from django.db import models


# Create your models here.


class iconCat (models.Model):
    name = models.CharField(max_length=32)
    png = models.CharField(max_length=16)

    def __str__ (self):
        return self.name

class rangeCat (models.Model):
    name = models.CharField(max_length=32)
    color = models.CharField(max_length=6)

    def __str__ (self):
        return self.name

class Category (models.Model):
    name = models.CharField(max_length=32)

    def __str__ (self):
        return self.name

class Post(models.Model):
    title =models.TextField(max_length=80)
    text = HTMLField() 

    cat = models.ForeignKey(Category, related_name='post', null=False, blank=True)
    active = models.BooleanField(default = False)
    order = models.CharField(max_length=3)
    icon =models.ForeignKey(iconCat, related_name='postStart', null=True, blank=True)
    interval =models.TextField(max_length=80, null=True, blank=True)
    startcat = models.ForeignKey(rangeCat, related_name='postStart', null=True, blank=True)
    endcat = models.ForeignKey(rangeCat, related_name='postEnd', null=True, blank=True)

    class Meta:
        ordering = ["order"]

    def __str__ (self):
        return self.name

class roomFac(models.Model):
    name = models.CharField(max_length=32)
    png = models.CharField(max_length=16)

    def __str__ (self):
        return self.name


class catRent (models.Model):
    name = models.CharField(max_length=32)

    def __str__ (self):
        return self.name
        
class Renting(models.Model):
    title =models.TextField(max_length=80)
    text = HTMLField() 

    cat = models.ForeignKey(catRent, related_name='rent', null=False, blank=True)
    facilites = models.ManyToManyField(roomFac, related_name='rent', null=False, blank=True)
    
    active = models.BooleanField(default = False)
    order = models.CharField(max_length=3)
    icon = models.TextField(max_length=80,null=True, blank=True)

    class Meta:
        ordering = ["order"]


class imgRent (models.Model):
    description = models.TextField(max_length=180,null=True, )
    content = models.ImageField() 
    room = models.ForeignKey(Renting, related_name='images', null=True, blank=True)

    def __str__ (self):
        return self.description


class Booking(models.Model):
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    room = models.ForeignKey(Renting, related_name='booking', null=False, blank=True)
    notes = models.TextField(max_length=180,null=True, )
    contacts_mail = models.EmailField(null=False,max_length=254)
    checkin_time = models.TimeField(null=True)
    approved = models.BooleanField(default= False)
