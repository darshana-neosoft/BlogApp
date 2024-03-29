# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-13 14:12
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_name', models.CharField(blank=True, max_length=600)),
                ('blog_content', models.CharField(blank=True, max_length=5000)),
                ('row_status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE', max_length=50)),
                ('created_by', models.CharField(blank=True, max_length=250)),
                ('updated_by', models.CharField(blank=True, max_length=250)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2016, 7, 13, 14, 12, 44, 514311))),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('blog_comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_comment_name', models.CharField(blank=True, max_length=600)),
                ('blog_comment_content', models.CharField(blank=True, max_length=5000)),
                ('row_status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE', max_length=50)),
                ('created_by', models.CharField(blank=True, max_length=250)),
                ('updated_by', models.CharField(blank=True, max_length=250)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2016, 7, 13, 14, 12, 44, 516879))),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogLikes',
            fields=[
                ('blog_comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_comment_name', models.CharField(blank=True, max_length=600)),
                ('blog_comment_content', models.CharField(blank=True, max_length=5000)),
                ('row_status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE', max_length=50)),
                ('created_by', models.CharField(blank=True, max_length=250)),
                ('updated_by', models.CharField(blank=True, max_length=250)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2016, 7, 13, 14, 12, 44, 519227))),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('blog_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bloggerapp.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_first_name', models.CharField(blank=True, max_length=250)),
                ('user_last_name', models.CharField(blank=True, max_length=250)),
                ('user_email_id', models.CharField(blank=True, max_length=250)),
                ('user_mobile_no', models.CharField(blank=True, max_length=50)),
                ('user_image', models.FileField(blank=True, max_length=500, null=True, upload_to='user_image')),
                ('row_status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE', max_length=50)),
                ('created_by', models.CharField(blank=True, max_length=250)),
                ('updated_by', models.CharField(blank=True, max_length=250)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2016, 7, 13, 14, 12, 44, 511814))),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='bloglikes',
            name='blog_like_owner',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bloggerapp.BlogUser'),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='blog_comment_owner',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bloggerapp.BlogUser'),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='blog_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bloggerapp.Blog'),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_owner',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bloggerapp.BlogUser'),
        ),
    ]
