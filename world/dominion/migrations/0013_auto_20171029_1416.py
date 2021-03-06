# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-29 14:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


# can't access Class constants in migrations, so we need to copy them here. No way around the DRY violation, sadly.
# Ticket constants
RESOLVED = 3
CLOSED = 4
# CrisisAction constants
PUBLISHED = 5
DRAFT = 0


def set_status(apps, schema_editor):
    CrisisAction = apps.get_model("dominion", "CrisisAction")
    CrisisAction.objects.filter(story="").update(status=DRAFT)
    for action in CrisisAction.objects.exclude(story=""):
        action.status = PUBLISHED
        if not action.update:
            action.update = action.crisis.upates.last()
        action.save()


def convert_storyactions(apps, schema_editor):
    Ticket = apps.get_model("helpdesk", "Ticket")
    CrisisAction = apps.get_model("dominion", "CrisisAction")
    for ticket in Ticket.objects.filter(queue__slug__iexact="story"):
        if ticket.status in (RESOLVED, CLOSED):
            status = PUBLISHED
        else:
            status = DRAFT
        dompc = ticket.submitting_player.Dominion
        gm = ticket.assigned_to
        actions = ticket.description or ""
        story = ticket.resolution or ""
        topic = ticket.title
        date_submitted = ticket.db_date_created
        action = CrisisAction(
            dompc=dompc,
            actions=actions,
            gm=gm,
            story=story,
            status=status,
            topic=topic,
            date_submitted=date_submitted,
        )
        action.save()
        for player in ticket.participants.all():
            action.assisting_actions.create(dompc=player.Dominion)


def complete_orders(apps, schema_editor):
    Orders = apps.get_model("dominion", "Orders")
    Orders.objects.filter(action__status=PUBLISHED).update(complete=True)


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("helpdesk", "0009_auto_20170521_1705"),
        ("character", "0019_auto_20171029_1416"),
        ("dominion", "0012_auto_20170920_0148"),
    ]

    operations = [
        migrations.RenameField(
            model_name="crisisaction",
            old_name="secret_action",
            new_name="secret_actions",
        ),
        migrations.AlterField(
            model_name="crisisaction",
            name="action",
            field=models.TextField(
                blank=True,
                help_text=b"The writeup the player submits of their actions, used for GMing.",
            ),
        ),
        migrations.RenameField(
            model_name="crisisaction", old_name="action", new_name="actions"
        ),
        migrations.RemoveField(
            model_name="crisisaction",
            name="rolls",
        ),
        migrations.RemoveField(
            model_name="crisisaction",
            name="sent",
        ),
        migrations.AlterField(
            model_name="crisisactionassistant",
            name="action",
            field=models.TextField(
                blank=True,
                help_text=b"The writeup the player submits of their actions, used for GMing.",
            ),
        ),
        migrations.RenameField(
            model_name="crisisactionassistant", old_name="action", new_name="actions"
        ),
        migrations.RemoveField(
            model_name="crisisactionassistant",
            name="can_see_secret",
        ),
        migrations.AlterField(
            model_name="crisisactionassistant",
            name="secret_action",
            field=models.TextField(
                blank=True, verbose_name=b"Secret actions the player is taking"
            ),
        ),
        migrations.RenameField(
            model_name="crisisactionassistant",
            old_name="secret_action",
            new_name="secret_actions",
        ),
        migrations.RemoveField(
            model_name="crisisactionassistant",
            name="share_secret",
        ),
        migrations.AddField(
            model_name="actionoocquestion",
            name="action_assist",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="dominion.CrisisActionAssistant",
            ),
        ),
        migrations.AddField(
            model_name="actionoocquestion",
            name="is_intent",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="actionoocquestion",
            name="action",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="dominion.CrisisAction",
            ),
        ),
        migrations.AddField(
            model_name="crisisaction",
            name="action_points",
            field=models.PositiveSmallIntegerField(
                blank=0,
                default=0,
                help_text=b"How many action points spent by player/assistants.",
            ),
        ),
        migrations.AddField(
            model_name="crisisaction",
            name="attending",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="crisisaction",
            name="category",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, b"Unknown"),
                    (1, b"Combat"),
                    (2, b"Support"),
                    (3, b"Sabotage"),
                    (4, b"Diplomacy"),
                    (5, b"Scouting"),
                    (6, b"Research"),
                ],
                default=0,
            ),
        ),
        migrations.AddField(
            model_name="crisisaction",
            name="date_submitted",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="crisisaction",
            name="difficulty",
            field=models.SmallIntegerField(blank=0, default=0),
        ),
        migrations.AddField(
            model_name="crisisaction",
            name="editable",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="crisisaction",
            name="gemit",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="actions",
                to="character.StoryEmit",
            ),
        ),
        migrations.AddField(
            model_name="crisisaction",
            name="gm",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="gmd_actions",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="crisisaction",
            name="prefer_offscreen",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="crisisaction",
            name="roll",
            field=models.SmallIntegerField(
                blank=True, default=-9999, help_text=b"Current dice roll"
            ),
        ),
        migrations.AddField(
            model_name="crisisaction",
            name="secret_story",
            field=models.TextField(
                blank=True, verbose_name=b"Any secret story written for the player"
            ),
        ),
        migrations.AddField(
            model_name="crisisaction",
            name="skill_used",
            field=models.CharField(
                blank=True,
                default=b"investigation",
                help_text=b"The skill the player chose to use",
                max_length=80,
            ),
        ),
        migrations.AddField(
            model_name="crisisaction",
            name="stat_used",
            field=models.CharField(
                blank=True,
                default=b"perception",
                help_text=b"The stat the player chose to use",
                max_length=80,
            ),
        ),
        migrations.AddField(
            model_name="crisisaction",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, b"Draft"),
                    (1, b"Needs Player Input"),
                    (2, b"Needs GM Input"),
                    (3, b"Cancelled"),
                    (4, b"Pending Publish"),
                    (5, b"Published"),
                ],
                default=0,
            ),
        ),
        migrations.AddField(
            model_name="crisisaction",
            name="topic",
            field=models.CharField(
                blank=True, help_text=b"Keywords or tldr or title", max_length=255
            ),
        ),
        migrations.AddField(
            model_name="crisisaction",
            name="traitor",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="crisisactionassistant",
            name="action_points",
            field=models.PositiveSmallIntegerField(
                blank=0,
                default=0,
                help_text=b"How many action points spent by player/assistants.",
            ),
        ),
        migrations.AddField(
            model_name="crisisactionassistant",
            name="attending",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="crisisactionassistant",
            name="date_submitted",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="crisisactionassistant",
            name="economic",
            field=models.PositiveSmallIntegerField(
                blank=0,
                default=0,
                help_text=b"Additional economic resources added by the player",
            ),
        ),
        migrations.AddField(
            model_name="crisisactionassistant",
            name="editable",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="crisisactionassistant",
            name="military",
            field=models.PositiveSmallIntegerField(
                blank=0,
                default=0,
                help_text=b"Additional military resources added by the player",
            ),
        ),
        migrations.AddField(
            model_name="crisisactionassistant",
            name="roll",
            field=models.SmallIntegerField(
                blank=True, default=-9999, help_text=b"Current dice roll"
            ),
        ),
        migrations.AddField(
            model_name="crisisactionassistant",
            name="silver",
            field=models.PositiveSmallIntegerField(
                blank=0, default=0, help_text=b"Additional silver added by the player"
            ),
        ),
        migrations.AddField(
            model_name="crisisactionassistant",
            name="skill_used",
            field=models.CharField(
                blank=True,
                default=b"investigation",
                help_text=b"The skill the player chose to use",
                max_length=80,
            ),
        ),
        migrations.AddField(
            model_name="crisisactionassistant",
            name="social",
            field=models.PositiveSmallIntegerField(
                blank=0,
                default=0,
                help_text=b"Additional social resources added by the player",
            ),
        ),
        migrations.AddField(
            model_name="crisisactionassistant",
            name="stat_used",
            field=models.CharField(
                blank=True,
                default=b"perception",
                help_text=b"The stat the player chose to use",
                max_length=80,
            ),
        ),
        migrations.AddField(
            model_name="crisisactionassistant",
            name="topic",
            field=models.CharField(
                blank=True, help_text=b"Keywords or tldr or title", max_length=255
            ),
        ),
        migrations.AddField(
            model_name="crisisactionassistant",
            name="traitor",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="crisisupdate",
            name="episode",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="crisis_updates",
                to="character.Episode",
            ),
        ),
        migrations.AddField(
            model_name="orders",
            name="action_assist",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to="dominion.CrisisActionAssistant",
            ),
        ),
        migrations.AlterField(
            model_name="crisisaction",
            name="gm_notes",
            field=models.TextField(
                blank=True, verbose_name=b"Any ooc notes for other GMs"
            ),
        ),
        migrations.AlterField(
            model_name="crisisaction",
            name="public",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="militaryunit",
            name="unit_type",
            field=models.PositiveSmallIntegerField(
                blank=0,
                choices=[
                    (0, b"Infantry"),
                    (1, b"Pike"),
                    (2, b"Cavalry"),
                    (3, b"Archers"),
                    (4, b"Longship"),
                    (5, b"Siege Weapon"),
                    (6, b"Galley"),
                    (8, b"Cog"),
                    (7, b"Dromond"),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="orgunitmodifiers",
            name="unit_type",
            field=models.PositiveSmallIntegerField(
                blank=0,
                choices=[
                    (0, b"Infantry"),
                    (1, b"Pike"),
                    (2, b"Cavalry"),
                    (3, b"Archers"),
                    (4, b"Longship"),
                    (5, b"Siege Weapon"),
                    (6, b"Galley"),
                    (8, b"Cog"),
                    (7, b"Dromond"),
                ],
                default=0,
            ),
        ),
        migrations.RunPython(set_status),
        migrations.RunPython(convert_storyactions),
        migrations.RunPython(complete_orders),
    ]
