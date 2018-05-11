# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import common.validators
from django.db import migrations, models
import django.db.models.deletion
import jobs.managers


class Migration(migrations.Migration):

    dependencies = [
        ('redirect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='redirect',
            name='internal',
            field=models.BooleanField(default=False),
        ),
    ]
