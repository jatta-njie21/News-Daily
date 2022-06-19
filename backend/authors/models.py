from django.db import models

# Create your models here.

class Detail(models.Model):
    first_name   = models.CharField(max_length=25)
    last_name    = models.CharField(max_length=25)
    phone_number = models.IntegerField(unique=True)
    email        = models.EmailField()
    twitter      = models.URLField(blank=True, null=True)
    facebook     = models.URLField(blank=True, null=True)
    Instagram    = models.URLField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)


    def __str__(self):
        return self.email
