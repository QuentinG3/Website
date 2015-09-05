# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lolbet', '0007_summonersname_lastgamecheck'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summonersname',
            name='lastGameCheck',
        ),
        migrations.AddField(
            model_name='streamer',
            name='lastGameCheck',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 5, 12, 17, 33, 292915, tzinfo=utc)),
        ),
    ]
