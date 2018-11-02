from django.db import models
import datetime as dt
from ckeditor.fields import RichTextField

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

    description = models.CharField(max_length =200,  blank=True, null=True)
    introduction_releasedate = RichTextField(blank=True, null=True)
    introduction_releasedate_image = models.CharField(max_length =200,  blank=True, null=True)
    performance_price = RichTextField(blank=True, null=True)
    performance_price_image = models.CharField(max_length =200,  blank=True, null=True)
    design_hardware = RichTextField(blank=True, null=True)
    design_hardware_image = models.CharField(max_length =200,  blank=True, null=True)
    software_os_softwarefeatures = RichTextField(blank=True, null=True)
    software_os_softwarefeatures_image = models.CharField(max_length =200,  blank=True, null=True)
    display = RichTextField(blank=True, null=True)
    display_image = models.CharField(max_length =200,  blank=True, null=True)
    batterylife = RichTextField(blank=True, null=True)
    batterylife_image = models.CharField(max_length =200,  blank=True, null=True)
    camera = RichTextField(blank=True, null=True)
    camera_image = models.CharField(max_length =200,  blank=True, null=True)
    competition = RichTextField(blank=True, null=True)
    competition_image = models.CharField(max_length =200,  blank=True, null=True)
    pros = RichTextField(blank=True, null=True)
    pros_image = models.CharField(max_length =200,  blank=True, null=True)
    cons = RichTextField(blank=True, null=True)
    cons_image = models.CharField(max_length =200,  blank=True, null=True)
    verdict = RichTextField(blank=True, null=True)

    title = models.CharField(max_length =60,  blank=True, null=True)
    network2G = RichTextField(max_length =100,  blank=True, null=True)
    network3G = RichTextField(max_length =100,  blank=True, null=True)
    network4G = RichTextField(max_length =100,  blank=True, null=True)
    gprsandedge = RichTextField(max_length = 60,  blank=True, null=True)
    launchannounced = RichTextField(max_length =60,  blank=True, null=True)
    launchavailable = RichTextField(max_length = 60,  blank=True, null=True)
    bodydimensions = RichTextField(max_length = 60,  blank=True, null=True)
    bodyweight = RichTextField(max_length = 60,  blank=True, null=True)
    bodybuild = RichTextField(max_length =60,   blank=True, null=True)
    bodysim = RichTextField(max_length =60,   blank=True, null=True)
    displaytype = RichTextField(max_length =60,   blank=True, null=True)
    displaysize = RichTextField(max_length =60,  blank=True, null=True)
    displayresolution = RichTextField(max_length =60,  blank=True, null=True)
    displaymultitouch = RichTextField(max_length =60,  blank=True, null=True)
    displayprotection = RichTextField(max_length =60,  blank=True, null=True)
    platformos = RichTextField(max_length =60,  blank=True, null=True)
    platformchipset = RichTextField(max_length =60,  blank=True, null=True)
    platformcpu = RichTextField(max_length =60,  blank=True, null=True)
    platformgpu = RichTextField(max_length =60,  blank=True, null=True)
    memorycardslot = RichTextField(max_length =60,  blank=True, null=True)
    internalmemory = RichTextField(max_length =60,  blank=True, null=True)
    maincameradual = RichTextField(max_length =60,  blank=True, null=True)
    maincamerafeatures = RichTextField(max_length =60,  blank=True, null=True)
    maincameravideo = RichTextField(max_length =60,  blank=True, null=True)
    selfiecameradual = RichTextField(max_length =60,  blank=True, null=True)
    selfiecamerafeatures = RichTextField(max_length =60,  blank=True, null=True)
    selfiecameravideo = RichTextField(max_length =60,  blank=True, null=True)
    soundalerttypes = RichTextField(max_length =60,  blank=True, null=True)
    soundloudspeaker = RichTextField(max_length =60,  blank=True, null=True)
    soundheadphonejack = RichTextField(max_length =60,  blank=True, null=True)
    commswlan = RichTextField(max_length =60,  blank=True, null=True)
    commsbluetooth = RichTextField(max_length =60,  blank=True, null=True)
    commsgps = RichTextField(max_length =60,  blank=True, null=True)
    commsnfc = RichTextField(max_length =60,  blank=True, null=True)
    commsradio = RichTextField(max_length =60,  blank=True, null=True)
    commsusb = RichTextField(max_length =60,  blank=True, null=True)
    featuressensors = RichTextField(max_length =60,  blank=True, null=True)
    featuresmessaging = RichTextField(max_length =60,  blank=True, null=True)
    featuresbrowser = RichTextField(max_length =60,  blank=True, null=True)
    battery =  RichTextField(max_length =60,  blank=True, null=True)
    devicecolors = RichTextField(max_length =60,  blank=True, null=True)
    performancetests = RichTextField(max_length =100,  blank=True, null=True)
    displaytest = RichTextField(max_length =100,  blank=True, null=True)
    cameratest = RichTextField(max_length =100,  blank=True, null=True)
    loudspeakertest = RichTextField(max_length =100,  blank=True, null=True)
    audiotest = RichTextField(max_length =100,  blank=True, null=True)
    batterytest = RichTextField(max_length =100,  blank=True, null=True)
    priceinkenya = RichTextField(max_length =60,  blank=True, null=True)
    priceinnigeria = RichTextField(max_length =60,  blank=True, null=True)
    priceinsouthafrica = RichTextField(max_length =60, blank=True, null=True)
    otherfeatures = RichTextField()
    phone_image = models.ImageField(upload_to = 'phonesimages/',  blank=True, null=True)

    editor = models.ForeignKey(Editor, on_delete= models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    @classmethod
    def allphones(cls):
        # phones = cls.objects.filter(pub_date__range=["2018-10-01", "2018-10-27"])
        phones = cls.objects.filter().order_by('-id')[:500]
        return phones

    @classmethod
    def nokia_phones(cls):
        nokia = cls.objects.filter(title__icontains = 'nokia')
        return nokia

    @classmethod
    def tecno_phones(cls):
        tecno = cls.objects.filter(title__icontains = 'tecno')
        return tecno

    @classmethod
    def infinix_phones(cls):
        infinix = cls.objects.filter(title__icontains = 'infinix')
        return infinix

    @classmethod
    def samsung_phones(cls):
        samsung = cls.objects.filter(title__icontains = 'samsung')
        return samsung

    @classmethod
    def iphone_phones(cls):
        iphone = cls.objects.filter(title__icontains = 'iphone')
        return iphone

    @classmethod
    def huawei_phones(cls):
        huawei = cls.objects.filter(title__icontains = 'huawei')
        return huawei

    @classmethod
    def search_by_title(cls, search_term):
        phones = cls.objects.filter(title__icontains=search_term)
        return phones

    @classmethod
    def latest_phones(cls):
        # latest = cls.objects.all()[:5]
        # latest = cls.objects.filter(pub_date__range=["2018-10-01", "2018-12-31"])[:5]
        latest = cls.objects.filter().order_by('-id')[:10]
        return latest

    @classmethod
    def popular_phones(cls):
        popular = cls.objects.filter(otherfeatures__icontains='popular').filter(pub_date__range=["2018-10-01", "2018-12-31"])[:5]
        return popular
    # @classmethod
    # def allphones(cls):
    #     phones = cls.objects.filter(pub_date__range=["2018-10-01", "2018-10-27"])
        # phones = cls.objects.all()[5:10]
    #     # phones = cls.objects.filter(title__icontains = 'Nokia')
    #     return phones
    #

    #
    # @classmethod
    # def search_by_title(cls,search_phone_term):
    #     phones = cls.objects.filter(title__icontains=search_phone_term)
    #     return phones


class Meta:
    ordering = ['name']
