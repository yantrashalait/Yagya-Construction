# Generated by Django 2.2.5 on 2019-09-16 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0031_projectoverview'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutionpage',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='solutionpage',
            name='heading',
            field=models.TextField(blank=True, null=True),
        ),
    ]