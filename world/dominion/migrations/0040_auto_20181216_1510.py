# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-16 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dominion", "0039_prestigetier"),
    ]

    operations = [
        migrations.AddField(
            model_name="prestigeadjustment",
            name="long_reason",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="prestigecategory",
            name="description",
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
