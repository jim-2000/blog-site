from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.FileField()
    details = models.TextField()
    def __str__(self):
        return self.name.username


class catagory(models.Model):
    name = models.CharField(max_length = 100)
    post_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.name


class article(models.Model):
    article_author = models.ForeignKey(author, on_delete= models.CASCADE)
    title = models.CharField(max_length = 100)
    image = models.FileField()
    body = models.TextField()
    highlight = models.CharField( max_length = 150) 
    post_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    post_update = models.DateTimeField(auto_now=True, auto_now_add=False)
    catagory= models.ForeignKey(catagory, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
        
    def get_single_url(self):
        return reverse('tube:Single', kwargs={"id":self.id})

class comment(models.Model):
    post =models.ForeignKey(article , on_delete= models.CASCADE)
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 50)
    post_comment = models.TextField()

    def __str__(self):
        return self.post.title
    

    
