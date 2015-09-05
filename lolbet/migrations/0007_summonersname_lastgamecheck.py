# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lolbet', '0006_profil_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='summonersname',
            name='lastGameCheck',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 5, 11, 39, 55, 794253, tzinfo=utc)),
        ),
    ]
