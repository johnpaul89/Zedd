from django.shortcuts import render
from .getjson import nationTitle, nationDate, nationArticle
import json
from Phones.models import Article

# Create your views here.
def zedd(request):

    title = nationTitle
    date = nationDate
    article = nationArticle

    phones = Article.allphones()

    return render(request, 'base.html', {"phones": phones, "title": title, "date": date, "article": article})
