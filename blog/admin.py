from django.contrib import admin
from .models import Category,Posts,PublishedPosts



admin.site.register(Category)


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display  = ['author','category','title','publish']
    
    
admin.site.register(PublishedPosts)