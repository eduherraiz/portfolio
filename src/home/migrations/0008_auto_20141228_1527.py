# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20141228_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('short_description', models.TextField(blank=True)),
                ('long_description', models.TextField(blank=True)),
                ('free_code_url', models.URLField(blank=True)),
                ('image', models.ImageField(upload_to=b'', blank=True)),
                ('important_project', models.BooleanField(default=False)),
                ('old_project', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='personal',
            name='projects',
            field=models.ManyToManyField(to='home.Project', blank=True),
            preserve_default=True,
        ),
    ]
