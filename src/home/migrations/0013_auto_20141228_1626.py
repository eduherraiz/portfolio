# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20141228_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(default=b'NOR', max_length=3, choices=[(b'IMP', b'Important'), (b'OLD', b'Old'), (b'NOR', b'Normal')]),
        ),
    ]
