# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150528_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='answers',
            field=models.CharField(max_length=250),
            preserve_default=True,
        ),
    ]
