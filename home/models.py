from django.db import models

# Create your models here.
class Message(models.Model):
    name					= models.CharField(max_length=100,null=True,blank=True)
    email					= models.CharField(max_length=100,null=True,blank=True)
    subject					= models.CharField(max_length=100,null=True,blank=True)
    message					= models.CharField(max_length=1000,null=True,blank=True)
    date_submited			= models.DateTimeField(verbose_name='date submited', auto_now_add=True)

    def __str__(self):
        return self.name