from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date,timezone

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name     
        
    def get_absolute_url(self):
        return reverse('home')
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()   
    category = models.CharField(max_length=255,default='General')
    post_date = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self) -> str:
        return self.title + ' | ' + str(self.author)    
        
    def get_absolute_url(self):
        return reverse('home')
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)  
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    text = models.TextField()
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'