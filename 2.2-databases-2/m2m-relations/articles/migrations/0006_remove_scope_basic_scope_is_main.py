# Generated by Django 4.2.6 on 2023-11-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_scope_basic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scope',
            name='basic',
        ),
        migrations.AddField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
    ]
