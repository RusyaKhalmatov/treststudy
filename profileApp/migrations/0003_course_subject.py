# Generated by Django 3.1.1 on 2020-10-19 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0002_auto_20201013_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ManyToManyField(to='profileApp.Subject'),
        ),
    ]
