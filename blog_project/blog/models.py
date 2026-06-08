from django.db import models
from django.utils.text import slugify
from django.urls import reverse
class blog(models.Model):
    title = models.CharField(max_length=100)
    short_des = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    slug = models.SlugField(default="")

    def name_link(self):
        return reverse('det_blog' , args=[self.slug]) 
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

