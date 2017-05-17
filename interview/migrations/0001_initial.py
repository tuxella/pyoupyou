# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import interview.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=30, verbose_name='Phone')),
            ],
        ),
        migrations.CreateModel(
            name='ContractType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('has_duration', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('document_type', models.CharField(choices=[('CV', 'CV'), ('CL', 'Cover Letter'), ('OT', 'Others')], max_length=2)),
                ('content', models.FileField(upload_to=interview.models.document_path)),
                ('still_valid', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_state', models.CharField(choices=[('NP', 'NEED PLANIFICATION'), ('PL', 'PLANNED'), ('GO', 'GO'), ('NO', 'NO')], max_length=3, verbose_name='next state')),
                ('rank', models.IntegerField(blank=True, null=True, verbose_name='Rank')),
                ('planned_date', models.DateTimeField(blank=True, null=True, verbose_name='Planned date')),
                ('minute', models.TextField(blank=True, verbose_name='Minute')),
                ('minute_format', models.CharField(choices=[('md', 'Markdown'), ('rst', 'ReStructured Text')], default='md', max_length=3)),
                ('next_interview_goal', models.TextField(blank=True, verbose_name='Next interview goal')),
            ],
            options={
                'ordering': ['process', 'rank'],
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End date')),
                ('salary_expectation', models.IntegerField(blank=True, null=True, verbose_name='Salary expectation (k€)')),
                ('contract_duration', models.PositiveIntegerField(blank=True, null=True, verbose_name='Contract duration in month')),
                ('contract_start_date', models.DateField(blank=True, null=True)),
                ('closed_reason', models.CharField(choices=[('OP', 'Open'), ('NG', 'Last interviewer interupt process'), ('CD', 'Candidate declined our offer'), ('HI', 'Candidate accepted our offer'), ('NO', 'Closed - other reason')], default='OP', max_length=3, verbose_name='Closed reason')),
                ('closed_comment', models.TextField(blank=True, verbose_name='Closed comment')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.Candidate')),
                ('contract_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='interview.ContractType')),
            ],
        ),
        migrations.CreateModel(
            name='Sources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SourcesCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='sources',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.SourcesCategory'),
        ),
        migrations.AddField(
            model_name='process',
            name='sources',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='interview.Sources'),
        ),
    ]
