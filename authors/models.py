from django.db import models
from common.models import TimeStamp
from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver


class Author(TimeStamp):
    full_name = models.CharField(max_length=255,verbose_name='Full Name')
    email     = models.EmailField()
    
    class Meta:
        verbose_name_plural = 'Author'
        
    def __str__(self):
        return self.full_name
    
    
class AuthorProfile(TimeStamp):
    author        = models.OneToOneField(Author,on_delete=models.CASCADE)
    email         = models.EmailField()
    phone_number  = models.IntegerField(blank=True,null=True)
    nationality   = models.CharField(max_length=255,blank=True,null=True)
    website       = models.URLField(blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    
    class Meta:
        verbose_name_plural = 'Author Profile'
        
    def __str__(self):
        return str(self.author)
    
    @receiver(post_save, sender=Author)
    def create_author_profile_after_creating_new_author(sender,instance,created,**kwargs):
        try:
            if created:
                AuthorProfile.objects.create(
                    author = instance,
                    email  = instance.email,
                )
        except:
            return 'Author profile instance not created'