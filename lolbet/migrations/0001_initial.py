# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('gameId', models.IntegerField()),
                ('won', models.BooleanField()),
                ('amount', models.IntegerField(null=True)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('dateModification', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('gameId', models.BigIntegerField()),
                ('gameStartTime', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('championId', models.BigIntegerField()),
                ('spell1Id', models.BigIntegerField()),
                ('spell2Id', models.BigIntegerField()),
                ('summonerId', models.BigIntegerField()),
                ('teamId', models.BigIntegerField()),
                ('profilIcanId', models.BigIntegerField()),
                ('game', models.ForeignKey(to='lolbet.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('elo', models.IntegerField(default=1200)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Streamer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('channelName', models.CharField(max_length=100)),
                ('online', models.BooleanField(default=False)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('dateModification', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SummonersName',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('nameId', models.BigIntegerField(null=True)),
                ('region', models.CharField(max_length=5)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('dateModification', models.DateTimeField(auto_now=True)),
                ('streamer', models.ForeignKey(to='lolbet.Streamer')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='summonersName',
            field=models.OneToOneField(to='lolbet.SummonersName'),
        ),
        migrations.AddField(
            model_name='bet',
            name='summonersName',
            field=models.ForeignKey(to='lolbet.SummonersName'),
        ),
        migrations.AddField(
            model_name='bet',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
