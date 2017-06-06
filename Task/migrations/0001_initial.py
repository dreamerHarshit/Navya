# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('permission_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('role_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='role_map_permission',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('permission_id', models.ForeignKey(to='Task.Permission')),
                ('role_id', models.ForeignKey(to='Task.Role')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='user_map_role',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('role_id', models.ForeignKey(to='Task.Role')),
                ('user_id', models.ForeignKey(to='Task.User')),
            ],
        ),
    ]
