# Generated by Django 2.2.5 on 2019-09-09 06:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0018_auto_20190909_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
