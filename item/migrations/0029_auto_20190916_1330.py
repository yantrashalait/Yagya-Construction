# Generated by Django 2.2.5 on 2019-09-16 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0028_auto_20190916_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='description1',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='description2',
            new_name='organization_heading',
        ),
    ]
