# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20141227_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='welcome_message',
            field=models.TextField(blank=True),
        ),
    ]
