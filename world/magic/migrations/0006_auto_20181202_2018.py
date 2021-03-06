# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-02 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("magic", "0005_magic_system_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Condition",
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
                ("name", models.CharField(max_length=40)),
                ("description", models.TextField(blank=True, null=True)),
                ("auto_discover", models.BooleanField(default=False)),
                (
                    "required_resonance",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text=b"If auto_discover is set, the Condition will automatically be gained when you have this much resonance in the associated node.",
                        null=True,
                    ),
                ),
                (
                    "roll_stat",
                    models.CharField(
                        default=b"Will",
                        help_text=b"The stat to roll to avoid this condition.",
                        max_length=20,
                    ),
                ),
                (
                    "roll_skill",
                    models.CharField(
                        default=b"Occult",
                        help_text=b"The skill to roll to avoid this condition.",
                        max_length=25,
                    ),
                ),
                (
                    "roll_base_difficulty",
                    models.PositiveSmallIntegerField(
                        default=30,
                        help_text=b"The base difficulty, which will be modified by effect strength and resonance of the attached node.",
                    ),
                ),
                (
                    "positive_condition",
                    models.BooleanField(
                        default=False,
                        help_text=b"If true, then succeeding the roll triggers this Condition; if false, failing does.",
                    ),
                ),
                ("emit_room", models.TextField(blank=True, null=True)),
                ("emit_self", models.TextField(blank=True, null=True)),
                (
                    "affinity",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="magic.Affinity",
                    ),
                ),
                (
                    "alignment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="magic.Alignment",
                    ),
                ),
                (
                    "effect",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="magic.Effect"
                    ),
                ),
                (
                    "node",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="conditions",
                        to="magic.SkillNode",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PractitionerCondition",
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
                ("gm_notes", models.TextField(blank=True, null=True)),
                (
                    "condition",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="afflicted",
                        to="magic.Condition",
                    ),
                ),
                (
                    "practitioner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="conditions",
                        to="magic.Practitioner",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="skillnoderesonance",
            name="practicing",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="working",
            name="gm_strength",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text=b"The base 'strength' of this magic, when it's a GM'd working.",
                null=True,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="practitionercondition",
            unique_together=set([("practitioner", "condition")]),
        ),
    ]
