from django.db import models

# Create your models here.
class ShowMe(models.Model):
    description = models.CharField(default='add a description',max_length=100)
    image = models.ImageField(default='default.png',upload_to='images/')
    title = models.CharField(default='title',max_length=10)

    def __str__(self):
        return self.title