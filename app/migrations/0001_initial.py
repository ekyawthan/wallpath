# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user_name', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=40)),
                ('question1', models.IntegerField()),
                ('question2', models.IntegerField()),
                ('question3', models.IntegerField()),
                ('question4', models.IntegerField()),
                ('question5', models.IntegerField()),
                ('question6', models.IntegerField()),
                ('question7', models.IntegerField()),
                ('question8', models.IntegerField()),
                ('question9', models.IntegerField()),
                ('question10', models.IntegerField()),
                ('question11', models.IntegerField()),
                ('question12', models.IntegerField()),
                ('delay_counter', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
