# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20141228_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='description_ca',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='description_en',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='description_es',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
