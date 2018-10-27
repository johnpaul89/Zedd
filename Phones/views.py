from django.shortcuts import render
from .models import PhoneArticle
from News.models import NewsArticle

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def available_phones(request):
    phones = PhoneArticle.allphones()
    return render(request, 'devices/phones.html', {"phones":phones})

def nokia_device(request):
    nokia = PhoneArticle.nokia_phones()
    return render(request, 'devices/Phones/nokia.html', {"nokia": nokia})

def tecno_device(request):
    tecno = PhoneArticle.tecno_phones()
    return render(request, 'devices/Phones/tecno.html', {"tecno": tecno})

def infinix_device(request):
    infinix = PhoneArticle.infinix_phones()
    return render(request, 'devices/Phones/infinix.html', {"infinix": infinix})

def samsung_device(request):
    samsung = PhoneArticle.samsung_phones()
    return render(request, 'devices/Phones/samsung.html', {"samsung": samsung})

def iphone_device(request):
    iphone = PhoneArticle.iphone_phones()
    return render(request, 'devices/Phones/iphone.html', {"iphone": iphone})

def huawei_device(request):
    huawei = PhoneArticle.huawei_phones()
    return render(request, 'devices/Phones/huawei.html', {"huawei": huawei})

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

        return render(request, 'news/search.html', {"message_phone": message_phone, "message_news": message_news, "phone_articles": searched_phone_article, "news_articles": searched_news_articles})

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
