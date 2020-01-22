# Generated by Django 2.2.6 on 2020-01-22 06:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.TextField(blank=True, null=True)),
                ('project_description', models.TextField()),
                ('client_name', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('sector', models.CharField(blank=True, max_length=100, null=True)),
                ('project_status', models.IntegerField(blank=True, choices=[(1, 'Upcoming'), (2, 'Ongoing'), (3, 'Completed')], null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': '2. Projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectOverView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': '1. Project Page Contents',
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Image size: width: 900px height: 879px', upload_to='project/')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='project_page.Project')),
            ],
        ),
    ]
