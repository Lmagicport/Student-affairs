# Generated by Django 3.1.2 on 2020-11-13 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affairstudent', '0002_auto_20201113_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentstudent',
            name='StuAge',
            field=models.IntegerField(),
        ),
    ]
