# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lolbet', '0005_player_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='username',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
