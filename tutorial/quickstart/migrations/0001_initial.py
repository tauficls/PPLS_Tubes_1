# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-13 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id_customer', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('alamat', models.TextField()),
                ('notelp', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id_item', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('kategori', models.CharField(max_length=25)),
                ('jenis', models.CharField(max_length=25)),
                ('weight', models.IntegerField(default=0)),
                ('place', models.CharField(max_length=50)),
                ('id_seller', models.IntegerField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('sent_to', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('id_seller', models.IntegerField(max_length=50)),
                ('id_customer', models.IntegerField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id_seller', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('alamat', models.TextField()),
                ('notelp', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse_id', models.IntegerField(max_length=50)),
                ('name', models.CharField(max_length=10)),
                ('item_id', models.IntegerField(max_length=50)),
            ],
        ),
    ]
