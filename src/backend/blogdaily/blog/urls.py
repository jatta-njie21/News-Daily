from django.urls import path

from . import views


urlpatterns = [
    path('',views.index,name = "index"),
    path('authors',views.authors, name = "authors"),
    path('<int:blog_id>',views.details, name = "pk =blog_id"),
]
