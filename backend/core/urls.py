from django.contrib import admin
from django.urls import path
from .local_urls import local_urls

urlpatterns = [
    path('admin/', admin.site.urls),

]

admin.site.site_header = 'Blog-Daily'
admin.site.site_title  = 'Blog-Daily Admin Site'
admin.site.index_title = 'Blog-Daily Admin'
