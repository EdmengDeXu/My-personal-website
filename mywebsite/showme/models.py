from django.db import models

# Create your models here.
class ShowMe(models.Model):
    description = models.CharField(max_length=100)