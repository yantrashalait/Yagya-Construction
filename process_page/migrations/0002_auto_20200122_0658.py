# Generated by Django 2.2.6 on 2020-01-22 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='processpage',
            options={'verbose_name': '1. Process Page Content'},
        ),
        migrations.AlterModelOptions(
            name='processstep',
            options={'verbose_name': '2. Process Step'},
        ),
    ]
