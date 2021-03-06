# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("character", "0025_storyemit_orgs"),
        ("exploration", "0002_auto_20181105_1538"),
    ]

    operations = [
        migrations.CreateModel(
            name="Shardhaven",
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
                ("name", models.CharField(db_index=True, max_length=78)),
                ("description", models.TextField(max_length=4096)),
                ("required_clue_value", models.IntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ShardhavenClue",
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
                ("required", models.BooleanField(default=False)),
                (
                    "clue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_shardhavens",
                        to="character.Clue",
                    ),
                ),
                (
                    "shardhaven",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_clues",
                        to="exploration.Shardhaven",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ShardhavenDiscovery",
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
                ("discovered_on", models.DateTimeField(blank=True, null=True)),
                (
                    "discovery_method",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, b"Unknown"),
                            (1, b"Exploration"),
                            (2, b"Clues"),
                            (3, b"Staff Ex Machina"),
                        ],
                        default=0,
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shardhaven_discoveries",
                        to="dominion.PlayerOrNpc",
                    ),
                ),
                (
                    "shardhaven",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="exploration.Shardhaven",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Shardhaven Discoveries",
            },
        ),
        migrations.CreateModel(
            name="ShardhavenType",
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
                ("name", models.CharField(db_index=True, max_length=32)),
                ("description", models.TextField(max_length=2048)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="shardhavenlayout",
            name="haven",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="layouts",
                to="exploration.Shardhaven",
            ),
        ),
        migrations.AlterField(
            model_name="shardhavenlayout",
            name="haven_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="exploration.ShardhavenType",
            ),
        ),
        migrations.AddField(
            model_name="shardhaven",
            name="discovered_by",
            field=models.ManyToManyField(
                blank=True,
                related_name="discovered_shardhavens",
                through="exploration.ShardhavenDiscovery",
                to="dominion.PlayerOrNpc",
            ),
        ),
        migrations.AddField(
            model_name="shardhaven",
            name="haven_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="havens",
                to="exploration.ShardhavenType",
            ),
        ),
        migrations.AddField(
            model_name="shardhaven",
            name="location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shardhavens",
                to="dominion.MapLocation",
            ),
        ),
    ]
