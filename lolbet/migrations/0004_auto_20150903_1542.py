# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lolbet', '0003_profil_verifyage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='championId',
        ),
        migrations.RemoveField(
            model_name='player',
            name='profilIcanId',
        ),
        migrations.RemoveField(
            model_name='player',
            name='spell1Id',
        ),
        migrations.RemoveField(
            model_name='player',
            name='spell2Id',
        ),
        migrations.RemoveField(
            model_name='player',
            name='teamId',
        ),
        migrations.AddField(
            model_name='game',
            name='bannedChampions0',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='game',
            name='bannedChampions1',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='game',
            name='bannedChampions2',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='game',
            name='bannedChampions3',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='game',
            name='bannedChampions4',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='game',
            name='bannedChampions5',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='champion',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='division',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='leaguePoints',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='losses',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='spell1',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='spell2',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='tier',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='wins',
            field=models.BigIntegerField(null=True),
        ),
    ]
