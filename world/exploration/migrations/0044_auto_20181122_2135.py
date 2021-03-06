# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-22 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("exploration", "0043_auto_20181122_1409"),
    ]

    operations = [
        migrations.AlterField(
            model_name="monstercraftingdrops",
            name="material",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="monsters",
                to="dominion.CraftingMaterialType",
            ),
        ),
    ]
