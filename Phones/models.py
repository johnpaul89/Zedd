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

class Article(models.Model):
    title = models.CharField(max_length =60)
    network2G = models.CharField(max_length =100)
    network3G = models.CharField(max_length =100)
    network4G = models.CharField(max_length =100)
    gprsandedge = models.CharField(max_length = 60)
    launchannounced = models.CharField(max_length =60)
    launchavailable = models.CharField(max_length = 60)
    bodydimensions = models.CharField(max_length = 60)
    bodyweight = models.CharField(max_length = 60)
    bodybuild = models.CharField(max_length =60)
    bodysim = models.CharField(max_length =60)
    displaytype = models.CharField(max_length =60)
    displaysize = models.CharField(max_length =60)
    displayresolution = models.CharField(max_length =60)
    displaymultitouch = models.CharField(max_length =60)
    displayprotection = models.CharField(max_length =60)
    platformos = models.CharField(max_length =60)
    platformchipset = models.CharField(max_length =60)
    platformcpu = models.CharField(max_length =60)
    platformgpu = models.CharField(max_length =60)
    memorycardslot = models.CharField(max_length =60)
    internalmemory = models.CharField(max_length =60)
    maincameradual = models.CharField(max_length =60)
    maincamerafeatures = models.CharField(max_length =60)
    maincameravideo = models.CharField(max_length =60)
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
    phone_image = models.ImageField(upload_to = 'phonesimages/', default='DEFAULT VALUE', blank=True, null=True)

    editor = models.ForeignKey(Editor, on_delete= models.CASCADE)
    tags = models.ManyToManyField(tags)


    @classmethod
    def allphones(cls):
        # today = dt.date.today()
        phones = cls.objects.filter()
        return phones

    @classmethod
    def search_by_title(cls, search_term):
        phones = cls.objects.filter(title__icontains=search_term)
        return phones



class Meta:
    ordering = ['name']
