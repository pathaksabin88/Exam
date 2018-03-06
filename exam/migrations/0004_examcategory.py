# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-23 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_batchsectionsemester'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(choices=[('MID_TERM', 'MID TERM'), ('FINAL_TERM', 'FINAL TERM'), ('PRACTICAL', 'PRACTICAL')], default='MID_TERM', max_length=100)),
                ('batchSectionSemester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.BatchSectionSemester')),
            ],
        ),
    ]