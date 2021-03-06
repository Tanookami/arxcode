# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-02-11 04:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("character", "0009_investigation_roll"),
        ("dominion", "0007_tasksupporter_additional_points"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClueForOrg",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "clue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="org_discoveries",
                        to="character.Clue",
                    ),
                ),
                (
                    "org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="clue_discoveries",
                        to="dominion.Organization",
                    ),
                ),
                (
                    "revealed_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="clues_added_to_orgs",
                        to="character.RosterEntry",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CrisisActionAssistant",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "action",
                    models.TextField(
                        blank=True, verbose_name="What action the assistant is taking"
                    ),
                ),
                (
                    "crisis_action",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assisting_actions",
                        to="dominion.CrisisAction",
                    ),
                ),
                (
                    "dompc",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assisting_actions",
                        to="dominion.PlayerOrNpc",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="crisisaction",
            name="assistants",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="assisted_actions",
                through="dominion.CrisisActionAssistant",
                to="dominion.PlayerOrNpc",
            ),
        ),
        migrations.AddField(
            model_name="organization",
            name="clues",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="orgs",
                through="dominion.ClueForOrg",
                to="character.Clue",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="crisisactionassistant",
            unique_together=set([("crisis_action", "dompc")]),
        ),
        migrations.AlterUniqueTogether(
            name="cluefororg",
            unique_together=set([("clue", "org")]),
        ),
    ]
