# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-02 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demygram', '0003_post_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=255)),
                ('followed', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
