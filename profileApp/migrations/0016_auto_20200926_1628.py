# Generated by Django 3.1.1 on 2020-09-26 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0015_auto_20200926_1625'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='student',
            table='Students',
        ),
        migrations.AlterModelTable(
            name='userextend',
            table='UserExtend',
        ),
    ]
