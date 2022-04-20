from django.contrib import admin
from .models import Author,Post
# Register your models here.

class AuthorDisplay(admin.ModelAdmin):
    list_display = ("id","name","specialty","followers","email","telephone")

admin.site.register(Author,AuthorDisplay)
admin.site.register(Post)