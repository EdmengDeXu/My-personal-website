from django.db import models

# Create your models here.
class Blog(models.Model):
    date = models.DateField()
    image = models.ImageField(default='default.jpeg',upload_to='images/')
    title = models.CharField(default='title',max_length=50)
    text = models.TextField(default='your text')

    def __str__(self):
        return self.title

    def short_text(self):
        return self.text[:10] + '...'