from django.db import models

# Create your models here.
class baecha(models.Model):
    date = models.DateField(max_length = 20)
    customer = models.CharField(max_length = 30)
    bl = models.CharField(max_length = 20)
    pic = models.CharField(max_length = 10)
    status = models.CharField(max_length = 10)
    trc = models.CharField(max_length = 20)
    company = models.CharField(max_length = 20)
    etc = models.TextField(max_length = 256)