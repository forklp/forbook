# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-03 13:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_page', '0003_comment_model_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='model_pic',
        ),
    ]
