# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiantian_user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddress',
            old_name='u_rev_name',
            new_name='u_recv_name',
        ),
    ]
