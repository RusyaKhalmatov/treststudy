# Generated by Django 3.0.8 on 2020-09-09 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0003_auto_20200909_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextend',
            name='url',
            field=models.SlugField(default='<django.db.models.query_utils.DeferredAttribute object at 0x7f156cfe2580>', unique=True),
        ),
    ]
