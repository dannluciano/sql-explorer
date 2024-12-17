# Generated by Django 5.0.4 on 2024-08-27 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0027_query_few_shot'),
    ]

    operations = [
        migrations.AddField(
            model_name='promptlog',
            name='database_connection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='explorer.databaseconnection'),
        ),
        migrations.AddField(
            model_name='promptlog',
            name='user_request',
            field=models.TextField(blank=True),
        ),
    ]