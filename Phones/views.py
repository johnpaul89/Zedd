from django.shortcuts import render
from .models import Article

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def available_phones(request):
    phones = Article.allphones()
    return render(request, 'devices/phones.html', {"phones":phones})

def article(request, article_id):
    phones = Article.allphones()
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request, 'devices/article.html', {"article": article, "phones":phones })
