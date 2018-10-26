from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^mobile-phones', views.available_phones, name='allphones'),
    url('^article/(\d+)', views.article, name='phone-article'),
    url(r'^search/', views.search_results, name='search_results')
]
