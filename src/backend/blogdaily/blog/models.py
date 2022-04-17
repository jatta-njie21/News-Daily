from django.db import models

from blog.views import authors

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)
    followers = models.IntegerField(default=0)
    email = models.EmailField()
    telephone = models.IntegerField()
    
    def __str__(self):
        return f'{self.name} - {self.specialty}'
    
    
class Post(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="author")
    title = models.CharField(max_length=40, default=" ")
    post = models.CharField(max_length=500)
    isPublished = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.title} written by {Author.name}'