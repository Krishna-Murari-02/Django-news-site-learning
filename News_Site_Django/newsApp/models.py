from django.db import models
import datetime


# Create your models here.

class new(models.Model):
    news_name = models.CharField(max_length=500)
    news_category = models.CharField(max_length=50)
    news_subcategory = models.CharField(max_length=50)
    news_summery = models.CharField(max_length=500)
    news_author = models.CharField(max_length=50)
    news_updateTime = models.DateTimeField(default=datetime.datetime.now())
    news_image = models.ImageField(upload_to = './static/images')
    news_place = models.CharField(max_length=20)
    news_paragraph = models.TextField()



class Breaking(models.Model):
    breaking = models.CharField(max_length=100)
    
    
