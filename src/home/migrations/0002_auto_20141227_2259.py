# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='location',
            field=models.CharField(default='', max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personal',
            name='analytics_code',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='footer',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='link_blog_rss',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='link_facebook',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='link_github',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='link_googleplus',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='link_linkedin',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='link_location',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='link_twitter',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='link_vimeo',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='link_youtube',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='profession',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='welcome_message',
            field=models.TextField(blank=True),
        ),
    ]
