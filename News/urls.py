from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.zedd,name = 'home'),
    url('^article/(\d+)', views.news_article, name = 'NewsArticle')
]
