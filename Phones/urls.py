from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^mobile-phones', views.available_phones, name='allphones'),
    url('^article/(\d+)', views.article, name='phone-article'),
    url(r'^search/', views.search_results, name='search_results'),
    url('^all-nokia-phones', views.nokia_device, name='nokia_mobiles'),
    url('^all-tecno-phones', views.tecno_device, name='tecno_mobiles'),
    url('^all-infinix-phones', views.infinix_device, name='infinix_mobiles'),
    url('^all-samsung-phones', views.samsung_device, name='samsung_mobiles'),
    url('^all-iphone-phones', views.iphone_device, name='iphone_mobiles'),
    url('^all-huawei-phones', views.huawei_device, name='huawei_mobiles'),
]
