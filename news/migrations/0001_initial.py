# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 13:27
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'title', unique=True)),
                ('date', models.DateField()),
                ('content', models.TextField()),
                ('live', models.BooleanField(default=True, help_text=b'Only live sites with dates today or in the past will be shown.')),
            ],
            options={
                'ordering': ['-date'],
                'abstract': False,
            },
        ),
    ]
