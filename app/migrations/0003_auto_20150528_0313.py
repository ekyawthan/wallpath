# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_survey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='user_name',
            field=models.CharField(unique=True, max_length=40),
            preserve_default=True,
        ),
    ]
