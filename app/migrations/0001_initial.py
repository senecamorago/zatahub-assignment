# Generated by Django 4.2.11 on 2024-03-19 07:22

import app.flax_id.django.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', app.flax_id.django.fields.FlaxId(editable=False, max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=512)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', app.flax_id.django.fields.FlaxId(editable=False, max_length=16, primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, max_length=1024)),
                ('publish_transaction_id', models.CharField(max_length=512)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.meeting')),
            ],
        ),
    ]
