# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-05 17:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("character", "0012_auto_20170519_1646"),
    ]

    operations = [
        migrations.RenameField(
            model_name="firstcontact",
            old_name="wrote_journal",
            new_name="private",
        ),
        migrations.RemoveField(
            model_name="firstcontact",
            name="wrote_short_rel",
        ),
    ]
