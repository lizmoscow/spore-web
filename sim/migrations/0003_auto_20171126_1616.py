# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-26 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0002_jobidmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobidmodel',
            name='job_id',
        ),
        migrations.AddField(
            model_name='jobidmodel',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
