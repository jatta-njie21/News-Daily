from django.contrib import admin
from .models import Author,AuthorProfile


@admin.register(Author)
class AuthorDisplay(admin.ModelAdmin):
    list_display  = ['full_name','email']
    search_fields = ['full_name','email']
    
    
@admin.register(AuthorProfile)
class AuthorProfileDisplay(admin.ModelAdmin):
    list_display  = ['author','email','phone_number','nationality','website','date_of_birth']
    search_fields = ['email','phone_number','nationality']