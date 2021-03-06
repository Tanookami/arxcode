# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-01 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dominion", "0035_auto_20180831_0922"),
        ("character", "0032_theory_plots"),
    ]

    operations = [
        migrations.CreateModel(
            name="Goal",
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
                    "scope",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, b"Heartbreakingly Modest"),
                            (1, b"Modest"),
                            (2, b"Reasonable"),
                            (3, b"Ambitious"),
                            (4, b"Venomously Ambitious"),
                            (5, b"Megalomanic"),
                        ],
                        default=2,
                    ),
                ),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, b"Succeeded"),
                            (1, b"Failed"),
                            (2, b"Abandoned"),
                            (3, b"Dormant"),
                            (4, b"Active"),
                        ],
                        default=4,
                    ),
                ),
                (
                    "summary",
                    models.CharField(
                        max_length=80, verbose_name=b"Summary of the goal"
                    ),
                ),
                (
                    "description",
                    models.TextField(verbose_name=b"Detailed description of the goal"),
                ),
                (
                    "ooc_notes",
                    models.TextField(
                        blank=True,
                        verbose_name=b"Any OOC notes by the player about the goal",
                    ),
                ),
                (
                    "gm_notes",
                    models.TextField(
                        blank=True,
                        verbose_name=b"Notes by staff, not visible to the player",
                    ),
                ),
                (
                    "entry",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="goals",
                        to="character.RosterEntry",
                    ),
                ),
                (
                    "plot",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="goals",
                        to="dominion.Plot",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="GoalUpdate",
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
                ("player_summary", models.TextField(blank=True)),
                (
                    "result",
                    models.TextField(
                        blank=True,
                        verbose_name=b"IC description of the outcome for the player",
                    ),
                ),
                (
                    "gm_notes",
                    models.TextField(
                        blank=True,
                        verbose_name=b"OOC notes for staff about consequences",
                    ),
                ),
                ("db_date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "beat",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="goal_updates",
                        to="dominion.PlotUpdate",
                    ),
                ),
                (
                    "goal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="updates",
                        to="character.Goal",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
