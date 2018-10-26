from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

class tags(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class PhoneArticle(models.Model):
    title = models.CharField(max_length =60,  blank=True, null=True)
    network2G = models.CharField(max_length =100,  blank=True, null=True)
    network3G = models.CharField(max_length =100,  blank=True, null=True)
    network4G = models.CharField(max_length =100,  blank=True, null=True)
    gprsandedge = models.CharField(max_length = 60,  blank=True, null=True)
    launchannounced = models.CharField(max_length =60,  blank=True, null=True)
    launchavailable = models.CharField(max_length = 60,  blank=True, null=True)
    bodydimensions = models.CharField(max_length = 60,  blank=True, null=True)
    bodyweight = models.CharField(max_length = 60,  blank=True, null=True)
    bodybuild = models.CharField(max_length =60,   blank=True, null=True)
    bodysim = models.CharField(max_length =60,   blank=True, null=True)
    displaytype = models.CharField(max_length =60,   blank=True, null=True)
    displaysize = models.CharField(max_length =60,  blank=True, null=True)
    displayresolution = models.CharField(max_length =60,  blank=True, null=True)
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
    selfiecameradual = models.CharField(max_length =60,  blank=True, null=True)
    selfiecamerafeatures = models.CharField(max_length =60,  blank=True, null=True)
    selfiecameravideo = models.CharField(max_length =60,  blank=True, null=True)
    soundalerttypes = models.CharField(max_length =60,  blank=True, null=True)
    soundloudspeaker = models.CharField(max_length =60,  blank=True, null=True)
    soundheadphonejack = models.CharField(max_length =60,  blank=True, null=True)
    commswlan = models.CharField(max_length =60,  blank=True, null=True)
    commsbluetooth = models.CharField(max_length =60,  blank=True, null=True)
    commsgps = models.CharField(max_length =60,  blank=True, null=True)
    commsnfc = models.CharField(max_length =60,  blank=True, null=True)
    commsradio = models.CharField(max_length =60,  blank=True, null=True)
    commsusb = models.CharField(max_length =60,  blank=True, null=True)
    featuressensors = models.CharField(max_length =60,  blank=True, null=True)
    featuresmessaging = models.CharField(max_length =60,  blank=True, null=True)
    featuresbrowser = models.CharField(max_length =60,  blank=True, null=True)
    battery =  models.CharField(max_length =60,  blank=True, null=True)
    devicecolors = models.CharField(max_length =60,  blank=True, null=True)
    performancetests = models.CharField(max_length =100,  blank=True, null=True)
    displaytest = models.CharField(max_length =100,  blank=True, null=True)
    cameratest = models.CharField(max_length =100,  blank=True, null=True)
    loudspeakertest = models.CharField(max_length =100,  blank=True, null=True)
    audiotest = models.CharField(max_length =100,  blank=True, null=True)
    batterytest = models.CharField(max_length =100,  blank=True, null=True)
    priceinkenya = models.CharField(max_length =60,  blank=True, null=True)
    priceinnigeria = models.CharField(max_length =60,  blank=True, null=True)
    priceinsouthafrica = models.CharField(max_length =60, blank=True, null=True)
    otherfeatures = models.TextField()
    phone_image = models.ImageField(upload_to = 'phonesimages/',  blank=True, null=True)

    editor = models.ForeignKey(Editor, on_delete= models.CASCADE)
    tags = models.ManyToManyField(tags)
    # pub_date = models.DateTimeField(auto_now_add=True)


    @classmethod
    def allphones(cls):
        phones = cls.objects.filter()
        return phones

    @classmethod
    def search_by_title(cls, search_term):
        phones = cls.objects.filter(title__icontains=search_term)
        return phones



class Meta:
    ordering = ['name']
