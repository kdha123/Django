# Generated by Django 3.0.2 on 2020-01-29 06:13

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='question',
            table='question',
        ),
    ]