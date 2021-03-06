# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 18:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("exploration", "0006_auto_20181105_1851"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shardhavenlayoutexit",
            name="room_east",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exit_west",
                to="exploration.ShardhavenLayoutSquare",
            ),
        ),
        migrations.AlterField(
            model_name="shardhavenlayoutexit",
            name="room_north",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exit_south",
                to="exploration.ShardhavenLayoutSquare",
            ),
        ),
        migrations.AlterField(
            model_name="shardhavenlayoutexit",
            name="room_south",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exit_north",
                to="exploration.ShardhavenLayoutSquare",
            ),
        ),
        migrations.AlterField(
            model_name="shardhavenlayoutexit",
            name="room_west",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exit_east",
                to="exploration.ShardhavenLayoutSquare",
            ),
        ),
    ]
