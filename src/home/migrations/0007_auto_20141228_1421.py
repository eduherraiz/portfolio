# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20141228_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='personal',
            name='profession',
        ),
        migrations.AddField(
            model_name='personal',
            name='professions',
            field=models.ManyToManyField(to='home.Profession', blank=True),
            preserve_default=True,
        ),
    ]
