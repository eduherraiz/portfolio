# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20141228_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='normal',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
