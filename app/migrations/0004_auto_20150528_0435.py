# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150528_0313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.AlterField(
            model_name='patient',
            name='user_name',
            field=models.CharField(max_length=40, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='survey',
            name='author',
            field=models.CharField(max_length=40),
            preserve_default=True,
        ),
    ]
