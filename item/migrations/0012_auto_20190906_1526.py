# Generated by Django 2.2.5 on 2019-09-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0011_auto_20190906_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='slogan',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='slogan',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]