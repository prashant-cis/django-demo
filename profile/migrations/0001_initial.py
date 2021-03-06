# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 12:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('block', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Job Category')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaving_type', models.CharField(choices=[('own', 'My Own Home'), ('rent', 'I am Leaving here rented'), ('pg', 'I am Leaving here paying guest')], max_length=1)),
                ('name', models.CharField(max_length=200, verbose_name='Full Name')),
                ('mobile', models.CharField(max_length=15, verbose_name='Mobile Number')),
                ('permanent_address', models.CharField(max_length=2000, verbose_name='Permanent address')),
                ('dob', models.DateField(verbose_name='Date of birth')),
                ('doa', models.DateField(verbose_name='Date of Anniversary')),
                ('job_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='profile.JobCategory')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
