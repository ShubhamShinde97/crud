from django.db import models
from django.urls import reverse

# Create your models here.
class cumpany(models.Model):
    company_name=models.CharField(max_length=50)
    company_logo=models.FileField(null='True',blank='True')
    company_city=models.CharField(max_length=50)
    def __str__(self):
        return self.company_name
    def __get__absolute_url(self):
        return reverse('retrive',kwargs={"id": self.id})