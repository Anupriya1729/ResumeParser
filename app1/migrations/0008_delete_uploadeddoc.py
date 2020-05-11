# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20200411_0427'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadedDoc',
        ),
    ]
