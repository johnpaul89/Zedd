# Generated by Django 2.1.2 on 2018-10-23 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Phones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='bodybuild',
        ),
        migrations.RemoveField(
            model_name='article',
            name='bodysim',
        ),
        migrations.RemoveField(
            model_name='article',
            name='bodyweight',
        ),
        migrations.RemoveField(
            model_name='article',
            name='displaymultitouch',
        ),
        migrations.RemoveField(
            model_name='article',
            name='displayprotection',
        ),
        migrations.RemoveField(
            model_name='article',
            name='displayresolution',
        ),
        migrations.RemoveField(
            model_name='article',
            name='displaysize',
        ),
        migrations.RemoveField(
            model_name='article',
            name='displaytype',
        ),
        migrations.RemoveField(
            model_name='article',
            name='internalmemory',
        ),
        migrations.RemoveField(
            model_name='article',
            name='maincameradual',
        ),
        migrations.RemoveField(
            model_name='article',
            name='maincamerafeatures',
        ),
        migrations.RemoveField(
            model_name='article',
            name='maincameravideo',
        ),
        migrations.RemoveField(
            model_name='article',
            name='memorycardslot',
        ),
        migrations.RemoveField(
            model_name='article',
            name='platformchipset',
        ),
        migrations.RemoveField(
            model_name='article',
            name='platformcpu',
        ),
        migrations.RemoveField(
            model_name='article',
            name='platformgpu',
        ),
        migrations.RemoveField(
            model_name='article',
            name='platformos',
        ),
    ]