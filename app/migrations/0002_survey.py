# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answers', models.CharField(max_length=50)),
                ('choices', models.CharField(max_length=250)),
                ('delay_counter', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(to='app.Patient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
