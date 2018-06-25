# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('c_id', models.AutoField(serialize=False, primary_key=True, db_column=b'c_id')),
                ('c_name', models.CharField(default=b'', max_length=31, db_column=b'c_name')),
                ('c_address', models.TextField(default=b'', db_column=b'c_address')),
                ('c_city', models.CharField(default=b'', max_length=50, db_column=b'c_city')),
                ('c_email', models.BooleanField(default=True, db_column=b'c_email')),
                ('c_contact', models.BigIntegerField(db_column=b'c_contact', validators=[django.core.validators.MaxValueValidator(9999999999L)])),
            ],
        ),
    ]
