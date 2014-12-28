# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20141228_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='important_project',
            new_name='important',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='old_project',
            new_name='old',
        ),
    ]
