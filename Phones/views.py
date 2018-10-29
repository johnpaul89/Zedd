from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from .models import PhoneArticle
from News.models import NewsArticle

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def available_phones(request):
    phones = PhoneArticle.allphones()
    page = request.GET.get('page', 1)
    paginator = Paginator(phones, 4)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)

    return render(request, 'devices/phones.html', {'numbers': numbers})

# def available_phones(request):
#     phones = PhoneArticle.allphones()
#     numbers_list = range(1, 1000)
#     page = request.GET.get('page', 1)
#     paginator = Paginator(numbers_list, 1)
#     try:
#         numbers = paginator.page(phones)
#     except PageNotAnInteger:
#         numbers = paginator.page(1)
#     except EmptyPage:
#         numbers = paginator.page(paginator.num_pages)
#
#     return render(request,  'devices/phones.html', {"phones": phones, "numbers": numbers})

def nokia_device(request):
    nokia = PhoneArticle.nokia_phones()
    page = request.GET.get('page', 1)
    paginator = Paginator(nokia, 4)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)

    return render(request, 'devices/Phones/nokia.html', {"nokia": nokia, "numbers": numbers})

def tecno_device(request):
    tecno = PhoneArticle.tecno_phones()
    page = request.GET.get('page', 1)
    paginator = Paginator(tecno, 4)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)

    return render(request, 'devices/Phones/tecno.html', {"tecno": tecno, "numbers": numbers})

def infinix_device(request):
    infinix = PhoneArticle.infinix_phones()
    page = request.GET.get('page', 1)
    paginator = Paginator(infinix, 4)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)

    return render(request, 'devices/Phones/infinix.html', {"infinix": infinix, "numbers": numbers})

def samsung_device(request):
    samsung = PhoneArticle.samsung_phones()
    page = request.GET.get('page', 1)
    paginator = Paginator(samsung, 4)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'devices/Phones/samsung.html', {"samsung": samsung, "numbers": numbers})

def iphone_device(request):
    iphone = PhoneArticle.iphone_phones()
    page = request.GET.get('page', 1)
    paginator = Paginator(iphone, 4)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)

    return render(request, 'devices/Phones/iphone.html', {"iphone": iphone, "numbers": numbers})

def huawei_device(request):
    huawei = PhoneArticle.huawei_phones()
    page = request.GET.get('page', 1)
    paginator = Paginator(huawei, 4)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)

    return render(request, 'devices/Phones/huawei.html', {"huawei": huawei, "numbers": numbers})

def article(request, article_id):
    phones = PhoneArticle.allphones()
    try:
        article = PhoneArticle.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request, 'devices/article.html', {"article": article, "phones":phones })

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

        return render(request, 'news/search.html', {"message_phone": message_phone, "newsnumbers": newsnumbers, "numbers": numbers, "message_news": message_news, "phone_articles": searched_phone_article, "news_articles": searched_news_articles})

    else:
        message_phone = "You haven't searched for any term"
        message_news = "You haven't searched for any term"

        return render(request, 'news/search.html', {"message_phone": message_phone, "message_news": message_news})

# def search_phone_results(request):
#
#     if 'article' in request.GET and request.GET["article"]:
#         search_term = request.GET.get("article")
#         # searched_articles = NewsArticle.search_by_title(search_term)
#         searched_articles = Article.search_by_title(search_term)
#         message = search_term
#
#         return render(request, 'devices/search.html',{"message":message,"articles": searched_articles})
#
#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'devices/search.html',{"message":message})
