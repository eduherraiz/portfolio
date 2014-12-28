# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20141228_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='profession',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
