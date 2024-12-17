# Generated by Django 5.0.4 on 2024-08-03 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0022_databaseconnection_upload_fingerprint'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='database_connection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='explorer.databaseconnection'),
        ),
        migrations.AddField(
            model_name='querylog',
            name='database_connection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='explorer.databaseconnection'),
        ),
        migrations.AlterField(
            model_name='databaseconnection',
            name='engine',
            field=models.CharField(
                choices=[('django.db.backends.sqlite3', 'SQLite3'), ('django.db.backends.postgresql', 'PostgreSQL'),
                         ('django.db.backends.mysql', 'MySQL'), ('django.db.backends.oracle', 'Oracle'),
                         ('django.db.backends.mysql', 'MariaDB'), ('django_cockroachdb', 'CockroachDB'),
                         ('mssql', 'SQL Server (mssql-django)'), ('django_snowflake', 'Snowflake'),
                         ('django_connection', 'Django Connection')], max_length=255),
        ),
        migrations.AlterField(
            model_name='databaseconnection',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='databaseconnection',
            name='port',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='databaseconnection',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]