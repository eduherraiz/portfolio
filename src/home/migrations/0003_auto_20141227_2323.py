# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20141227_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='welcome_message',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
