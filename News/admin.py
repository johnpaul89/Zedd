from django.contrib import admin
from .models import NewsArticle,  tags

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(NewsArticle)
admin.site.register(tags)
