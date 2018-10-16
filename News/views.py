from django.shortcuts import render
from .getjson import nationTitle, nationDate, nationArticle
import json

# Create your views here.
def zedd(request):

    title = nationTitle
    date = nationDate
    article = nationArticle

    return render(request, 'base.html', {"title": title, "date": date, "article": article})
