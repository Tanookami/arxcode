# Generated by Django 2.2.9 on 2019-12-28 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("magic", "0009_auto_20181211_1716"),
    ]

    operations = [
        migrations.AlterField(
            model_name="affinity",
            name="opposed",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="magic.Affinity",
            ),
        ),
        migrations.AlterField(
            model_name="affinity",
            name="rank1_desc",
            field=models.CharField(default="spark", max_length=255),
        ),
        migrations.AlterField(
            model_name="affinity",
            name="rank2_desc",
            field=models.CharField(default="glimmer", max_length=255),
        ),
        migrations.AlterField(
            model_name="affinity",
            name="rank3_desc",
            field=models.CharField(default="glow", max_length=255),
        ),
        migrations.AlterField(
            model_name="affinity",
            name="rank4_desc",
            field=models.CharField(default="light", max_length=255),
        ),
        migrations.AlterField(
            model_name="affinity",
            name="rank5_desc",
            field=models.CharField(default="brilliance", max_length=255),
        ),
        migrations.AlterField(
            model_name="alchemicalmaterial",
            name="affinity",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="materials",
                to="magic.Affinity",
            ),
        ),
        migrations.AlterField(
            model_name="alchemicalmaterial",
            name="alignment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="magic.Alignment",
            ),
        ),
        migrations.AlterField(
            model_name="alignment",
            name="adjective",
            field=models.CharField(default="colorful", max_length=20),
        ),
        migrations.AlterField(
            model_name="condition",
            name="affinity",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="magic.Affinity",
            ),
        ),
        migrations.AlterField(
            model_name="condition",
            name="positive_condition",
            field=models.BooleanField(
                default=False,
                help_text="If true, then succeeding the roll triggers this Condition; if false, failing does.",
            ),
        ),
        migrations.AlterField(
            model_name="condition",
            name="required_resonance",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="If auto_discover is set, the Condition will automatically be gained when you have this much resonance in the associated node.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="condition",
            name="roll_base_difficulty",
            field=models.PositiveSmallIntegerField(
                default=30,
                help_text="The base difficulty, which will be modified by effect strength and resonance of the attached node.",
            ),
        ),
        migrations.AlterField(
            model_name="condition",
            name="roll_skill",
            field=models.CharField(
                default="Occult",
                help_text="The skill to roll to avoid this condition.",
                max_length=25,
            ),
        ),
        migrations.AlterField(
            model_name="condition",
            name="roll_stat",
            field=models.CharField(
                default="Will",
                help_text="The stat to roll to avoid this condition.",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="effect",
            name="affinity",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="magic.Affinity",
            ),
        ),
        migrations.AlterField(
            model_name="effect",
            name="antagonistic",
            field=models.BooleanField(
                default=False, help_text="Is this effect harmful to the target?"
            ),
        ),
        migrations.AlterField(
            model_name="effect",
            name="coded_effect",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Sight"),
                    (1, "Add Clue to Collection"),
                    (2, "Add Successes to A Global Tally"),
                    (3, "Add to Primum Value of Object"),
                    (4, "Absorb Primum from an Object"),
                    (5, "Attune to Object, Player, or Agent"),
                    (6, "Boost a Stat"),
                    (7, "Ward a Location"),
                    (9, "Heal a Character"),
                    (10, "Simply Emits Flavor Text"),
                    (11, "Temporarily Reveal an Exploration Map"),
                    (12, "Apply a Combat Condition"),
                    (13, "Remove a Combat Condition"),
                    (14, "Apply a Combat Effect"),
                    (15, "Remove a Combat Effect"),
                    (16, "Change the Weather"),
                    (17, "Anima Ritual"),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="effect",
            name="coded_params",
            field=models.CharField(
                blank=True,
                help_text="Parameters specific to the coded effect type.",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="effect",
            name="required_favor",
            field=models.PositiveIntegerField(
                default=0,
                help_text="A base amount of favor required to weave this effect.",
            ),
        ),
        migrations.AlterField(
            model_name="effect",
            name="target_type",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "None"),
                    (1, "Self"),
                    (2, "Character"),
                    (3, "Object"),
                    (4, "Player or Object"),
                    (5, "Clue"),
                    (6, "Location"),
                    (7, "Retainer"),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="effect",
            name="want_opposed",
            field=models.BooleanField(
                default=False,
                help_text="Is this effect more effective when used on an opposed affinity? (If not, it will be more effective when used on the same affinity.)",
            ),
        ),
        migrations.AlterField(
            model_name="practitioner",
            name="gesture",
            field=models.CharField(
                default="gestures expansively and energetically",
                help_text="Short descriptive fragment of how this practitioner casts.",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="practitioner",
            name="language",
            field=models.CharField(
                default="Arvani",
                help_text="The language in which this practitioner casts.",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="practitioner",
            name="magic_desc",
            field=models.TextField(
                blank=True,
                help_text="Additional text someone might see if they soulgaze this practitioner with high successes.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="practitioner",
            name="magic_desc_short",
            field=models.CharField(
                blank=True,
                help_text="A short description of someone's magic, to be included in a generated sentence",
                max_length=1024,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="practitioner",
            name="raw_affinity",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="magic.Affinity",
            ),
        ),
        migrations.AlterField(
            model_name="practitioner",
            name="raw_alignment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="magic.Alignment",
            ),
        ),
        migrations.AlterField(
            model_name="practitioner",
            name="sigil_desc",
            field=models.CharField(
                blank=True,
                help_text="What this person's magic looks for description as a signature (on wards and workings).",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="practitioner",
            name="sigil_emit",
            field=models.TextField(
                blank=True,
                help_text="The emit that's shown to mage-sight when this practitioner works magic.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="practitioner",
            name="skill",
            field=models.CharField(default="occult", max_length=40),
        ),
        migrations.AlterField(
            model_name="practitioner",
            name="stat",
            field=models.CharField(default="intellect", max_length=40),
        ),
        migrations.AlterField(
            model_name="practitioner",
            name="verb",
            field=models.CharField(
                default="chants",
                help_text="The verb (chants, sings, etc.) to describe this practitioner's casting style.",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="practitionereffect",
            name="learned_by",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Staff Fiat"), (1, "Teaching"), (2, "Discovery")],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="practitionerspell",
            name="learned_by",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Staff Fiat"), (1, "Teaching"), (2, "Discovery")],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="practitionerspell",
            name="success_msg",
            field=models.TextField(
                blank=True, help_text="Custom message for our version of the spell"
            ),
        ),
        migrations.AlterField(
            model_name="skillnode",
            name="affinity",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="nodes",
                to="magic.Affinity",
            ),
        ),
        migrations.AlterField(
            model_name="skillnode",
            name="affinity_default",
            field=models.BooleanField(
                default=False,
                help_text="Does this node function as the default for this affinity in its tree?",
            ),
        ),
        migrations.AlterField(
            model_name="skillnode",
            name="discovered_by_revelations",
            field=models.ManyToManyField(
                blank=True,
                help_text="If we discover these revelations, the node is automatically discovered.",
                related_name="nodes",
                to="character.Revelation",
            ),
        ),
        migrations.AlterField(
            model_name="skillnode",
            name="eyes_open",
            field=models.BooleanField(
                default=False,
                help_text="If set, then having this node open means someone's eyes are opened.",
            ),
        ),
        migrations.AlterField(
            model_name="skillnoderesonance",
            name="learned_by",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Staff Fiat"), (1, "Teaching"), (2, "Discovery")],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="spell",
            name="affinity",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="magic.Affinity",
            ),
        ),
        migrations.AlterField(
            model_name="spell",
            name="alignment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="magic.Alignment",
            ),
        ),
        migrations.AlterField(
            model_name="spell",
            name="discovered_by_clues",
            field=models.ManyToManyField(
                blank=True,
                help_text="If we discover any of these clues, the spell is automatically learned.",
                related_name="spells",
                to="character.Clue",
            ),
        ),
        migrations.AlterField(
            model_name="spell",
            name="extra_primum",
            field=models.PositiveSmallIntegerField(
                default=100,
                help_text="What percentage of a player's anima can they pull from external sources for this spell?  100% means they can pull exactly as much as their maximum anima.",
            ),
        ),
        migrations.AlterField(
            model_name="spell",
            name="required_favor",
            field=models.PositiveIntegerField(
                default=0,
                help_text="A base amount of favor required with Abyssal or Elysian to cast this spell.",
            ),
        ),
        migrations.AlterField(
            model_name="working",
            name="econ",
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="working",
            name="gm_cost",
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="working",
            name="gm_difficulty",
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="working",
            name="gm_strength",
            field=models.PositiveSmallIntegerField(
                blank=True,
                default=0,
                help_text="The base 'strength' of this magic, when it's a GM'd working.",
            ),
        ),
        migrations.AlterField(
            model_name="working",
            name="primum_at_perform",
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="working",
            name="quiet_level",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "None"), (1, "Mundane"), (2, "Total")], default=0
            ),
        ),
        migrations.AlterField(
            model_name="working",
            name="total_favor",
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="working",
            name="total_successes",
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="working",
            name="weave_affinity",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="magic.Affinity",
            ),
        ),
        migrations.AlterField(
            model_name="working",
            name="weave_alignment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="magic.Alignment",
            ),
        ),
        migrations.AlterField(
            model_name="working",
            name="weave_effect",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="magic.Effect",
            ),
        ),
        migrations.AlterField(
            model_name="workingparticipant",
            name="familiar",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="magic.FamiliarAttunement",
            ),
        ),
        migrations.AlterField(
            model_name="workingparticipant",
            name="tool",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="magic.Attunement",
            ),
        ),
    ]
