# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-01 13:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodname', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=4)),
                ('review', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('review', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='reviews',
        ),
        migrations.AddField(
            model_name='review',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant'),
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant'),
        ),
        migrations.AddField(
            model_name='deal',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant'),
        ),
    ]