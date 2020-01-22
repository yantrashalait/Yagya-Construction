# Generated by Django 2.2.6 on 2020-01-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.TextField(blank=True, null=True)),
                ('icon', models.ImageField(help_text='Image size: width=71px height=68px', upload_to='process/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SolutionPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(help_text='Image size: width=1220px height=711px', upload_to='solution/')),
                ('title', models.TextField(blank=True, null=True)),
                ('heading', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SolutionWeProvide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution_name', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(help_text='Image size: width=711px height=410px', upload_to='solution/')),
            ],
        ),
    ]
