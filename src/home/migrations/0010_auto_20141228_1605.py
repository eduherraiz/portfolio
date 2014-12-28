# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20141228_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='long_description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='short_description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
