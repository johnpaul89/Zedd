# Generated by Django 2.1.2 on 2018-10-31 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Phones', '0010_phonearticle_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phonearticle',
            old_name='recommendation',
            new_name='verdict',
        ),
    ]
