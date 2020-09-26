# Generated by Django 3.0.8 on 2020-09-09 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profileApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userextend',
            name='role_id',
        ),
        migrations.AlterField(
            model_name='student',
            name='u_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='u_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
