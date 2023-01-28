from django.contrib import admin
from .models import Category,Post,PublishedPosts



admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ['author','category','title','publish']
    
    
admin.site.register(PublishedPosts)