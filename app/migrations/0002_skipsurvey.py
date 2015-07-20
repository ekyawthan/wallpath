# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkipSurvey',
            fields=[
                ('user_name', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
