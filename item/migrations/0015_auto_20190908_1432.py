# Generated by Django 2.2.5 on 2019-09-08 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0014_auto_20190906_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.IntegerField(blank=True, choices=[(1, 'Upcoming'), (2, 'Ongoing'), (3, 'Completed')], null=True),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='number',
            field=models.CharField(max_length=50),
        ),
    ]
