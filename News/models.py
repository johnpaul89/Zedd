from django.db import models
import datetime as dt

class tags(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class NewsArticle(models.Model):
    source = models.CharField(max_length = 30)
    title = models.CharField(max_length = 200)
    articleUrl = models.CharField(max_length =120)
    imageUrl = models.CharField(max_length = 120)
    date = models.CharField(max_length = 60)
    article = models.TextField()

    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    @classmethod
    def allnews(cls):
        news = cls.objects.filter(pub_date__range=["2018-10-01", "2018-10-28"])
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news




class Meta:
    ordering = ['name']
