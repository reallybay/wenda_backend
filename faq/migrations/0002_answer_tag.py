# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='tag',
            field=models.CharField(max_length=500, default='no_tag', blank=True),
        ),
    ]
