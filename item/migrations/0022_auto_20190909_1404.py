# Generated by Django 2.2.5 on 2019-09-09 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0021_auto_20190909_1336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='description1',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='about',
            name='description2',
        ),
        migrations.RemoveField(
            model_name='about',
            name='description3',
        ),
    ]
