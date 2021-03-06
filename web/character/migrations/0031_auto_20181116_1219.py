# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-16 12:19
from __future__ import unicode_literals

from django.db import migrations, models


def replace_mysteries_without_through_model(apps, schema_editor):
    """
    Since LoreTopic is being merged with Revelation, we want to try to try to move over the data
    here. What we want to do is try to see if a LoreTopic shares a name with a Revelation. If so,
    we'll copy over the LoreTopic's desc directly to Revelation's gmnotes field. If not, we'll
    create a Revelation with the appropriate gm_notes and add its search tags to it.
    """
    Revelation = apps.get_model("character", "Revelation")
    Mystery = apps.get_model("character", "Mystery")
    RevelationForMystery = apps.get_model("character", "RevelationForMystery")
    RevelationMysteriesThrough = apps.get_model(
        "character", "Revelation_mysteries_added"
    )
    revelation_mysteries_bulk_create_list = []

    for rev_for_mystery in RevelationForMystery.objects.all():
        revelation_mysteries_bulk_create_list.append(
            RevelationMysteriesThrough(
                revelation=rev_for_mystery.revelation, mystery=rev_for_mystery.mystery
            )
        )
    RevelationMysteriesThrough.objects.bulk_create(
        revelation_mysteries_bulk_create_list
    )


class Migration(migrations.Migration):

    dependencies = [
        ("character", "0030_auto_20180828_0040"),
    ]

    operations = [
        migrations.AddField(
            model_name="revelation",
            name="mysteries_added",
            field=models.ManyToManyField(
                blank=True,
                help_text="Categories of revelations with summaries",
                related_name="revelations",
                to="character.Mystery",
            ),
        ),
        migrations.RunPython(replace_mysteries_without_through_model),
        migrations.RemoveField(
            model_name="revelationformystery",
            name="mystery",
        ),
        migrations.RemoveField(
            model_name="revelationformystery",
            name="revelation",
        ),
        migrations.AlterField(
            model_name="clue",
            name="clue_type",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Game Lore"), (1, "Vision"), (2, "Character Secret")],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="mystery",
            name="desc",
            field=models.TextField(
                blank=True,
                help_text="A summary of the lore of revelations for this category",
                verbose_name="Description",
            ),
        ),
        migrations.RemoveField(
            model_name="revelation",
            name="mysteries",
        ),
        migrations.DeleteModel(
            name="RevelationForMystery",
        ),
        migrations.RenameField(
            model_name="revelation", old_name="mysteries_added", new_name="mysteries"
        ),
    ]
