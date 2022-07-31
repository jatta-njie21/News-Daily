from django.contrib import admin
from django.urls import path
from .local_urls import local_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    
] + local_urls()

admin.site.site_header = 'Project_Name'
admin.site.site_title  = 'Project_Name Admin Site'
admin.site.index_title = 'Project_Name Admin'
