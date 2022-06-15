from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class Blog (models.Model):
    title=models.CharField(max_length=250)
    text=models.TextField()
    date=models.DateTimeField()
    image=models.ImageField(upload_to="img/%y")

    def __str__(self):
        return self.title




