from django.contrib import admin
from .models import Editor, PhoneArticle, tags

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

# Register your models here.
admin.site.register(Editor)
admin.site.register(PhoneArticle)
admin.site.register(tags)
