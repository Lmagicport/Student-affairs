# Generated by Django 3.1.2 on 2020-11-16 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('affairteacher', '0002_auto_20201113_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentteacher',
            name='TeaBirth',
        ),
    ]
