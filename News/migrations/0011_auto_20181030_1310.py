# Generated by Django 2.1.2 on 2018-10-30 13:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0010_auto_20181029_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='date',
            field=ckeditor.fields.RichTextField(max_length=80),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='source',
            field=ckeditor.fields.RichTextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=ckeditor.fields.RichTextField(max_length=50),
        ),
    ]
