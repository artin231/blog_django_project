from django.db import models
from django.utils.text import slugify

class blog(models.Model):
    title = models.CharField(max_length=100)
    short_des = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    slug = models.SlugField(default=slugify(title))