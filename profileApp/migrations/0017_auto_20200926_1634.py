# Generated by Django 3.1.1 on 2020-09-26 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0016_auto_20200926_1628'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='student',
            table='students',
        ),
        migrations.AlterModelTable(
            name='userextend',
            table='user_extend',
        ),
    ]
