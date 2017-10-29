# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-28 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ref', '0003_auto_20171028_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewer',
            name='interviewer_type',
            field=models.CharField(blank=True, choices=[('C', 'CONSULTANT'), ('E', 'EXTERNAL')], max_length=2, null=True, verbose_name='Interviewer Type'),
        ),
    ]