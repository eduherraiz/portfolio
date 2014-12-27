# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('profession', models.CharField(max_length=100)),
                ('link_linkedin', models.URLField()),
                ('link_twitter', models.URLField()),
                ('link_github', models.URLField()),
                ('link_facebook', models.URLField()),
                ('link_googleplus', models.URLField()),
                ('link_youtube', models.URLField()),
                ('link_vimeo', models.URLField()),
                ('welcome_message', models.TextField()),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=75)),
                ('link_location', models.URLField()),
                ('link_blog_rss', models.URLField()),
                ('footer', models.TextField()),
                ('analytics_code', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
