# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20141227_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='interval_profession',
            field=models.IntegerField(default=3000, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='num_blog_entries',
            field=models.IntegerField(default=3, blank=True),
            preserve_default=True,
        ),
    ]
