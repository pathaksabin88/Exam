# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-23 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_examcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examDate', models.DateField()),
                ('examCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.ExamCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facultyFullName', models.CharField(max_length=100)),
                ('facultyEmail', models.CharField(max_length=200)),
                ('facultyContactNumber', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FacultySubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectName', models.CharField(max_length=100)),
                ('semester', models.CharField(choices=[('SEMESTER_1', 'SEMESTER 1'), ('SEMESTER_2', 'SEMESTER 2'), ('SEMESTER_3', 'SEMESTER 3'), ('SEMESTER_4', 'SEMESTER 4'), ('SEMESTER_5', 'SEMESTER 5'), ('SEMESTER_6', 'SEMESTER 6'), ('SEMESTER_7', 'SEMESTER 7'), ('SEMESTER_8', 'SEMESTER 8')], default='SEMESTER_1', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='facultysubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Subject'),
        ),
        migrations.AddField(
            model_name='examinfo',
            name='facultySubject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.FacultySubject'),
        ),
    ]
