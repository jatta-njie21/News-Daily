from django.db import models
from common.models import *
from authors.models import Author
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    category    = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)

    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.category
    
    
class Post(TimeStamp):
    author   = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    title    = models.CharField(max_length=255)
    post     = models.TextField()
    publish  = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'All Posts'


class PublishedPosts(TimeStamp):
    post = models.OneToOneField(Post,on_delete=models.CASCADE)
    
    
    # @receiver(post_save, sender=Post)
    # def check_if_post_is_published(sender,instance,created,**kwargs):

    #     all_posts = Post.objects.all()
        
    #     for post in all_posts:
    #         if post.publish:
    #             PublishedPosts.objects.create(
    #                 post = post
    #             )
    
    class Meta:
        verbose_name_plural = 'Published Posts'
        
    def __str__(self):
        return str(self.post)    