# Generated by Django 3.2.13 on 2022-05-12 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.IntegerField(),
        ),
    ]