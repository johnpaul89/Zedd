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
    # pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def allnews(cls):
        news = cls.objects.filter()
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news

class PhoneArticle(models.Model):
    title = models.CharField(max_length =60)
    network2G = models.CharField(max_length =100)
    network3G = models.CharField(max_length =100)
    network4G = models.CharField(max_length =100)
    gprsandedge = models.CharField(max_length = 60)
    launchannounced = models.CharField(max_length =60)
    launchavailable = models.CharField(max_length = 60)
    bodydimensions = models.CharField(max_length = 60)
    bodyweight = models.CharField(max_length = 60, blank=True, null=True)
    bodybuild = models.CharField(max_length =60,   blank=True, null=True)
    bodysim = models.CharField(max_length =60,   blank=True, null=True)
    displaytype = models.CharField(max_length =60,  blank=True, null=True)
    displaysize = models.CharField(max_length =60, blank=True, null=True)
    displayresolution = models.CharField(max_length =60, blank=True, null=True)
    displaymultitouch = models.CharField(max_length =60,  blank=True, null=True)
    displayprotection = models.CharField(max_length =60,  blank=True, null=True)
    platformos = models.CharField(max_length =60,  blank=True, null=True)
    platformchipset = models.CharField(max_length =60,  blank=True, null=True)
    platformcpu = models.CharField(max_length =60,  blank=True, null=True)
    platformgpu = models.CharField(max_length =60,  blank=True, null=True)
    memorycardslot = models.CharField(max_length =60,  blank=True, null=True)
    internalmemory = models.CharField(max_length =60,  blank=True, null=True)
    maincameradual = models.CharField(max_length =60,  blank=True, null=True)
    maincamerafeatures = models.CharField(max_length =60,  blank=True, null=True)
    maincameravideo = models.CharField(max_length =60,  blank=True, null=True)
    selfiecameradual = models.CharField(max_length =60)
    selfiecamerafeatures = models.CharField(max_length =60)
    selfiecameravideo = models.CharField(max_length =60)
    soundalerttypes = models.CharField(max_length =60)
    soundloudspeaker = models.CharField(max_length =60)
    soundheadphonejack = models.CharField(max_length =60)
    commswlan = models.CharField(max_length =60)
    commsbluetooth = models.CharField(max_length =60)
    commsgps = models.CharField(max_length =60)
    commsnfc = models.CharField(max_length =60)
    commsradio = models.CharField(max_length =60)
    commsusb = models.CharField(max_length =60)
    featuressensors = models.CharField(max_length =60)
    featuresmessaging = models.CharField(max_length =60)
    featuresbrowser = models.CharField(max_length =60)
    battery =  models.CharField(max_length =60)
    devicecolors = models.CharField(max_length =60)
    performancetests = models.CharField(max_length =100)
    displaytest = models.CharField(max_length =100)
    cameratest = models.CharField(max_length =100)
    loudspeakertest = models.CharField(max_length =100)
    audiotest = models.CharField(max_length =100)
    batterytest = models.CharField(max_length =100)
    priceinkenya = models.CharField(max_length =60)
    priceinnigeria = models.CharField(max_length =60)
    priceinsouthafrica = models.CharField(max_length =60)
    otherfeatures = models.TextField()
    phone_image = models.ImageField(upload_to = 'phonesimages/',  blank=True, null=True)

    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    @classmethod
    def allphones(cls):
        phones = cls.objects.filter()
        return phones

    @classmethod
    def search_by_title(cls,search_phone_term):
        phones = cls.objects.filter(title__icontains=search_phone_term)
        return phones


class Meta:
    ordering = ['name']
