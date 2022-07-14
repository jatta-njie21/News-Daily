from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',csrf_exempt(GraphQLView.as_view(graphiql = True))),
]

admin.site.site_header = "Blog-Daily"
admin.site.site_title  = "Blog-Daily Admin Site"
admin.site.index_title = "Blog-Daily Admin"