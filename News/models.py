from django.db import models
import datetime as dt
from ckeditor.fields import RichTextField

class tags(models.Model):
    name = RichTextField(max_length = 50)

    def __str__(self):
        return self.name

class NewsArticle(models.Model):
    source = RichTextField(max_length = 20)
    title = models.CharField(max_length = 200)
    articleUrl = models.CharField(max_length =120)
    imageUrl = models.CharField(max_length = 120)
    date = RichTextField(max_length = 80)
    article = RichTextField()

    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    @classmethod
    def allnews(cls):
        # news = cls.objects.filter(pub_date__range=["2018-10-01", "2018-12-31"])
        news = cls.objects.filter().order_by('-id')[:500]
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news




class Meta:
    ordering = ['name']
