from django.db import models


# model for the articles
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

    class Meta:
        ordering = ['-created_at']