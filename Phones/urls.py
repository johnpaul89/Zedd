from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^zedd', views.available_phones, name='allphones'),
    url('^article/(\d+)', views.article, name='phone-article'),
]
