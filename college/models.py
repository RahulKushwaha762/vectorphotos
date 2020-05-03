from django.db import models

# Create your models here.

class Userdetails(models.Model):
    passw = models.CharField(max_length=100,default='',null=False)
    emailw = models.CharField(max_length=100,default='',null=False)
    userw = models.CharField(max_length=100, default='', null=False)

class Topics(models.Model):
    name = models.CharField(max_length=100,default='')
    total = models.IntegerField(default=0,null=False)
    temail = models.CharField(max_length=100,default='',null=False)

class Images(models.Model):
    email = models.CharField(max_length=100,default='',null=False)
    topic = models.CharField(max_length=100,default='',null=False)
    image = models.FileField(blank=True)
    name = models.CharField(max_length=100,default='')
    link = models.CharField(max_length=1000,default='')
    pdflink = models.CharField(max_length=1000,default='')
