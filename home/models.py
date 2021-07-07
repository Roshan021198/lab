from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime, date
from django.db.models.base import Model
from django.urls import reverse

# Create your models here.
class Message(models.Model):
    name					= models.CharField(max_length=100,null=True,blank=True)
    email					= models.CharField(max_length=100,null=True,blank=True)
    subject					= models.CharField(max_length=100,null=True,blank=True)
    message					= models.CharField(max_length=1000,null=True,blank=True)
    date_submited			= models.DateTimeField(verbose_name='date submited', auto_now_add=True)

    def __str__(self):
        return self.name




class Gallery(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    gallery_image=models.ImageField(null=True,blank=True,upload_to='images/')

    def __str__(self):
        return self.title




class Team(models.Model):
    name=models.CharField(max_length=225,null=True,blank=True)
    designation=models.CharField(max_length=300,null=True,blank=True)
    image=models.ImageField(null=True,blank=True,upload_to='images/')
    facebooklink=models.CharField(max_length=500,null=True,blank=True)
    instalink=models.CharField(max_length=500,null=True,blank=True)
    twiterlink=models.CharField(max_length=500,null=True,blank=True)
    linkdnlink=models.CharField(max_length=500,null=True,blank=True) 


    def __str__(self):
        return self.name


class News(models.Model):
    STATUS=(
        ('True','True'),
        ('False','False'),
    )
    title=models.CharField(max_length=225,null=True,blank=True)
    image=models.ImageField(null=True,blank=True,upload_to='images/')
    defination=models.CharField(max_length=300,null=True,blank=True)
    details=RichTextField(blank=True,null=True)
    status=models.CharField(max_length=10,choices=STATUS,null=True,blank=True)
    slug=models.SlugField(null=False,unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    upcoming_date=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    news_desc=models.TextField(blank=True)


    def __str__(self):
        return self.title

       







class Testimonials(models.Model):
    name=models.CharField(max_length=225,null=True,blank=True)
    designation=models.CharField(max_length=225,null=True,blank=True)
    quotes=models.CharField(max_length=1000,null=True,blank=True)
    image=models.ImageField(null=True,blank=True,upload_to='images/')


    def __str__(self):
        return self.name

class Ceategory(models.Model):
    category=models.CharField(max_length=225,null=True,blank=True)
    description=models.CharField(max_length=400,null=True,blank=True)
    icon=models.CharField(max_length=50,null=True,blank=True)


    def __str__(self):
        return self.category


class ServiceProduct(models.Model):
    category= models.ForeignKey(Ceategory,on_delete=models.CASCADE)
    productname=models.CharField(max_length=500,null=True,blank=True)
    productimage=models.ImageField(null=True,blank=True,upload_to='images/')
    description=RichTextField(blank=True,null=True)



    

    def __str__(self):
        return self.productname

    def image_tag(self):
        return mark_safe ('<img src="{}" height="50"/>'.format(self.productimage.url)) 

    image_tag.short_description='Image'    


class TariffChart(models.Model):
    machine = models.CharField(max_length=500,null=True,blank=True)
    working = models.CharField(max_length=500,null=True,blank=True)
    tariff = models.CharField(max_length=250,null=True,blank=True)
    tariff_per_hr = models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return self.machine
