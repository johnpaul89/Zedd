from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.zedd,name = 'home'),
    url('^news', views.all_news, name = 'allnews'),
    url('^article/(\d+)', views.news_article, name = 'NewsArticle'),
    url(r'^search/', views.search_results, name='search_results'),
    # url('^all-nokia-phones', views.nokia_device, name='nokiaphones'),
]
