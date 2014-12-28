# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20141228_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='footer_ca',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='footer_en',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='footer_es',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='welcome_message_ca',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='welcome_message_en',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='welcome_message_es',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
