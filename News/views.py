from django.shortcuts import render, redirect
from .models import NewsArticle, PhoneArticle
import datetime as dt

# Create your views here.
def zedd(request):

    date = dt.date.today()
    news = NewsArticle.allnews()
    phones = PhoneArticle.allphones()
    nokia = PhoneArticle.nokia_phones()

    return render(request, 'base.html', {"date": date, "news": news, "phones": phones, "nokia": nokia })

def all_news(request):

    date = dt.date.today()
    news = NewsArticle.allnews()

    return render(request, 'news/news.html', {"date": date, "news": news})

def news_article(request, article_id):
    try:
        article = NewsArticle.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()

    return render(request, 'news/article.html', {"article": article})

# def search_news_results(request):
#
#     if 'article' in request.GET and request.GET["article"]:
#         search_term = request.GET.get("article")
#         searched_articles = NewsArticle.search_by_title(search_term)
#         message = search_term
#
#         return render(request, 'news/search.html',{"message":message,"articles": searched_articles})
#
#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'news/search.html',{"message":message})

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_phone_term = request.GET.get("article")
        search_news_term = request.GET.get("article")
        searched_news_articles = NewsArticle.search_by_title(search_news_term)
        searched_phone_article = PhoneArticle.search_by_title(search_phone_term)

        message_phone = search_phone_term
        message_news = search_news_term

        return render(request, 'news/search.html', {"message_phone": message_phone, "message_news": message_news, "phone_articles": searched_phone_article, "news_articles": searched_news_articles})

    else:
        message_phone = "You haven't searched for any term"
        message_news = "You haven't searched for any term"

        return render(request, 'news/search.html', {"message_phone": message_phone, "message_news": message_news})
