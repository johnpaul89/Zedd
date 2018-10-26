# Generated by Django 2.1.2 on 2018-10-25 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_auto_20181025_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('network2G', models.CharField(max_length=100)),
                ('network3G', models.CharField(max_length=100)),
                ('network4G', models.CharField(max_length=100)),
                ('gprsandedge', models.CharField(max_length=60)),
                ('launchannounced', models.CharField(max_length=60)),
                ('launchavailable', models.CharField(max_length=60)),
                ('bodydimensions', models.CharField(max_length=60)),
                ('bodyweight', models.CharField(blank=True, default='DEFAULT VALUE', max_length=60, null=True)),
                ('bodybuild', models.CharField(blank=True, default='DEFAULT VALUE', max_length=60, null=True)),
                ('bodysim', models.CharField(blank=True, default='DEFAULT VALUE', max_length=60, null=True)),
                ('displaytype', models.CharField(blank=True, default='DEFAULT VALUE', max_length=60, null=True)),
                ('displaysize', models.CharField(blank=True, default='DEFAULT VALUE', max_length=60, null=True)),
                ('displayresolution', models.CharField(blank=True, default='DEFAULT VALUE', max_length=60, null=True)),
                ('displaymultitouch', models.CharField(blank=True, default='DEFAULT VALUE', max_length=60, null=True)),
                ('displayprotection', models.CharField(blank=True, default='DEFAULT VALUE', max_length=60, null=True)),
                ('platformos', models.CharField(blank=True, default='DEFAULT VALUE', max_length=60, null=True)),
                ('platformchipset', models.CharField(blank=True, default='DEFAULT VALUE', max_length=60, null=True)),
                ('platformcpu', models.CharField(blank=True, default='DEFAULT VALUE', max_length=60, null=True)),
                ('platformgpu', models.CharField(blank=True, default='DEFAULT VALUE', max_length=60, null=True)),
                ('memorycardslot', models.CharField(blank=True, default='DEFAULT VALUE', max_length=60, null=True)),
                ('internalmemory', models.CharField(blank=True, default='DEFAULT VALUE', max_length=60, null=True)),
                ('maincameradual', models.CharField(blank=True, default='DEFAULT VALUE', max_length=60, null=True)),
                ('maincamerafeatures', models.CharField(blank=True, default='DEFAULT VALUE', max_length=60, null=True)),
                ('maincameravideo', models.CharField(blank=True, default='DEFAULT VALUE', max_length=60, null=True)),
                ('selfiecameradual', models.CharField(max_length=60)),
                ('selfiecamerafeatures', models.CharField(max_length=60)),
                ('selfiecameravideo', models.CharField(max_length=60)),
                ('soundalerttypes', models.CharField(max_length=60)),
                ('soundloudspeaker', models.CharField(max_length=60)),
                ('soundheadphonejack', models.CharField(max_length=60)),
                ('commswlan', models.CharField(max_length=60)),
                ('commsbluetooth', models.CharField(max_length=60)),
                ('commsgps', models.CharField(max_length=60)),
                ('commsnfc', models.CharField(max_length=60)),
                ('commsradio', models.CharField(max_length=60)),
                ('commsusb', models.CharField(max_length=60)),
                ('featuressensors', models.CharField(max_length=60)),
                ('featuresmessaging', models.CharField(max_length=60)),
                ('featuresbrowser', models.CharField(max_length=60)),
                ('battery', models.CharField(max_length=60)),
                ('devicecolors', models.CharField(max_length=60)),
                ('performancetests', models.CharField(max_length=100)),
                ('displaytest', models.CharField(max_length=100)),
                ('cameratest', models.CharField(max_length=100)),
                ('loudspeakertest', models.CharField(max_length=100)),
                ('audiotest', models.CharField(max_length=100)),
                ('batterytest', models.CharField(max_length=100)),
                ('priceinkenya', models.CharField(max_length=60)),
                ('priceinnigeria', models.CharField(max_length=60)),
                ('priceinsouthafrica', models.CharField(max_length=60)),
                ('otherfeatures', models.TextField()),
                ('phone_image', models.ImageField(blank=True, default='DEFAULT VALUE', null=True, upload_to='phonesimages/')),
                ('tags', models.ManyToManyField(to='News.tags')),
            ],
        ),
        migrations.RenameModel(
            old_name='Article',
            new_name='NewsArticle',
        ),
    ]