from ast import Delete
from datetime import datetime
from time import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User , models.CASCADE)
    title = models.CharField(max_length=50) 
    content = models.TextField(max_length=800)
    img = models.ImageField(upload_to= 'post_image/', default='post_img/defuatl.png')
    created = models.DateTimeField(default=timezone.now())
    
     
    def __str__(self):
        return self.title
    
 