from django.shortcuts import render
from .models import NewsArticle, PhoneArticle
import datetime as dt

# Create your views here.
def zedd(request):

    date = dt.date.today()
    news = NewsArticle.allnews()
    phones = PhoneArticle.allphones()

    return render(request, 'base.html', {"date": date, "news": news, "phones": phones })

def news_article(request, article_id):
    try:
        article = NewsArticle.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()

    return render(request, 'news/article.html', {"article": article})
