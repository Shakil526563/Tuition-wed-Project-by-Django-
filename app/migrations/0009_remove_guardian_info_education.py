# Generated by Django 4.0.3 on 2022-04-01 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_guardian_info_delete_guardian_inf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guardian_info',
            name='Education',
        ),
    ]