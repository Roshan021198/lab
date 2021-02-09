from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime, date
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
    title=models.CharField(max_length=255)
    gallery_image=models.ImageField(null=True,blank=True,upload_to='images/')

    def __str__(self):
        return self.title




class Team(models.Model):
    name=models.CharField(max_length=225)
    designation=models.CharField(max_length=300)
    image=models.ImageField(null=True,blank=True,upload_to='images/')
    facebooklink=models.CharField(max_length=300)
    instalink=models.CharField(max_length=300)
    twiterlink=models.CharField(max_length=300)
    linkdnlink=models.CharField(max_length=300) 


    def __str__(self):
        return self.name


class News(models.Model):
    STATUS=(
        ('True','True'),
        ('False','False'),
    )
    title=models.CharField(max_length=225)
    image=models.ImageField(null=True,blank=True,upload_to='images/')
    defination=models.CharField(max_length=300)
    details=RichTextField(blank=True,null=True)
    status=models.CharField(max_length=10,choices=STATUS)
    slug=models.SlugField(null=False,unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    upcoming_date=models.DateField(auto_now_add=False,auto_now=False,blank=True)


    def __str__(self):
        return self.title

       







class Testimonials(models.Model):
    name=models.CharField(max_length=225)
    designation=models.CharField(max_length=225)
    quotes=models.CharField(max_length=1000)
    image=models.ImageField(null=True,blank=True,upload_to='images/')


    def __str__(self):
        return self.name

class Ceategory(models.Model):
    category=models.CharField(max_length=225)
    description=models.CharField(max_length=400)
    icon=models.CharField(max_length=50,null=True,blank=True)


    def __str__(self):
        return self.category


class ServiceProduct(models.Model):
    category= models.ForeignKey(Ceategory,on_delete=models.CASCADE)
    productname=models.CharField(max_length=255)
    productdescription=models.CharField(max_length=2000)
    productimage=models.ImageField(null=True,blank=True,upload_to='images/')


    

    def __str__(self):
        return self.productname

    def image_tag(self):
        return mark_safe ('<img src="{}" height="50"/>'.format(self.productimage.url)) 

    image_tag.short_description='Image'    
