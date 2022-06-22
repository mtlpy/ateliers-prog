from django.db import models

# Create your models here.


class Book(models.Model):
    # id
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True)