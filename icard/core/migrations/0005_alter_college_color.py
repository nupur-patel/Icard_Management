# Generated by Django 3.2.13 on 2022-05-14 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='color',
            field=models.CharField(max_length=7),
        ),
    ]
