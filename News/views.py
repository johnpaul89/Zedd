from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from .models import NewsArticle
from Phones.models import PhoneArticle
import datetime as dt

# Create your views here.
def zedd(request):

    date = dt.date.today()
    latest = PhoneArticle.latest_phones()
    popular = PhoneArticle.popular_phones()
    news = NewsArticle.allnews()
    phones = PhoneArticle.allphones()
    page = request.GET.get('page', 1)
    paginator = Paginator(news, 4)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)

    return render(request, 'base.html', {"date": date, "latest": latest, "popular": popular, "news": news, "phones": phones, "numbers": numbers })

# def nokia_device(request):
#     nokia = PhoneArticle.nokia_phones()
#     return render(request, 'devices/Phones/nokia.html', {"nokia": nokia})

def all_news(request):

    date = dt.date.today()
    news = NewsArticle.allnews()
    page = request.GET.get('page', 1)
    paginator = Paginator(news, 4)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)

    return render(request, 'news/news.html', {"date": date, "news": news, "numbers": numbers})

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

        page = request.GET.get('page', 1)
        paginator = Paginator(searched_phone_article, 4)
        try:
            numbers = paginator.page(page)
        except PageNotAnInteger:
            numbers = paginator.page(1)
        except EmptyPage:
            numbers = paginator.page(paginator.num_pages)

        page = request.GET.get('page', 1)
        paginator = Paginator(searched_news_articles, 4)
        try:
            newsnumbers = paginator.page(page)
        except PageNotAnInteger:
            numbers = paginator.page(1)
        except EmptyPage:
            numbers = paginator.page(paginator.num_pages)

        return render(request, 'news/search.html', {"message_phone": message_phone, "newsnumbers": newsnumbers, "numbers": numbers,  "message_news": message_news, "phone_articles": searched_phone_article, "news_articles": searched_news_articles})

    else:
        message_phone = "You haven't searched for any term"
        message_news = "You haven't searched for any term"

        return render(request, 'news/search.html', {"message_phone": message_phone, "message_news": message_news})
