# Generated by Django 2.2.6 on 2020-01-22 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': '2. Project'},
        ),
        migrations.AlterModelOptions(
            name='projectoverview',
            options={'verbose_name': '1. Project Page Content'},
        ),
    ]
