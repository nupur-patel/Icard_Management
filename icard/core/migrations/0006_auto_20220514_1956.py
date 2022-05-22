# Generated by Django 3.2.13 on 2022-05-14 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_college_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='college_name',
            new_name='college',
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
