# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lolbet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='streamer',
            name='preview',
            field=models.CharField(max_length=200, default=''),
        ),
        migrations.AddField(
            model_name='streamer',
            name='status',
            field=models.CharField(max_length=200, default=''),
        ),
        migrations.AddField(
            model_name='streamer',
            name='viewers',
            field=models.IntegerField(default=0),
        ),
    ]
