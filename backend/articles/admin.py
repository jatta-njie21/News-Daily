from django.contrib import admin


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display  = ['title', 'created_at', 'updated_at']
    search_fields = ['title', 'body']