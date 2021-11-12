from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    autor= models.CharField(max_length=100)
    data_publi = models.DateTimeField(blank=True, null=True)
    upload = models.FileField(upload_to='uploads/')

class Blog(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)      


