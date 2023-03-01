from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images', default="noimage.jpg")
    description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    publishedDate = models.DateTimeField('date published')
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

class Tag(models.Model):

    def __str__(self):
        return self.name

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)



