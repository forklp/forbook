# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-03 13:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0003_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='model_pic',
        ),
    ]