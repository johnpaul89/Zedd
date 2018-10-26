from django.contrib import admin
from .models import NewsArticle, PhoneArticle, tags

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(NewsArticle)
admin.site.register(PhoneArticle)
admin.site.register(tags)
