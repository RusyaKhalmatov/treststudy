# Generated by Django 3.1.1 on 2020-10-07 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0004_auto_20201007_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='url',
            field=models.SlugField(null=True, unique=True),
        ),
    ]