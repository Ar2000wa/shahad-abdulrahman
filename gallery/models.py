from django.db import models

# Create your models here.


class Beauty (models.Model):
    name=models.CharField(max_length=150)
    image=models.ImageField(upload_to="beauty/",null=True)



class Fashion (models.Model):
    name=models.CharField(max_length=150)
    image=models.ImageField(upload_to="fashion/",null=True)



class Weddings (models.Model):
    name=models.CharField(max_length=150)
    image=models.ImageField(upload_to="weddings/",null=True)


