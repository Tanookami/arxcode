# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dominion", "0015_auto_20171109_2244"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rpevent",
            name="crisis",
        ),
        migrations.AddField(
            model_name="rpevent",
            name="actions",
            field=models.ManyToManyField(
                blank=True, related_name="events", to="dominion.CrisisAction"
            ),
        ),
    ]
