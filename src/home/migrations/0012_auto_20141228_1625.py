# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_project_normal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='important',
        ),
        migrations.RemoveField(
            model_name='project',
            name='normal',
        ),
        migrations.RemoveField(
            model_name='project',
            name='old',
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.CharField(default=b'NOR', max_length=1, choices=[(b'IMP', b'Important'), (b'OLD', b'Old'), (b'NOR', b'Normal')]),
            preserve_default=True,
        ),
    ]
