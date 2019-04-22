from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title
