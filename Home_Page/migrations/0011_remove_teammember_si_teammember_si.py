# Generated by Django 4.2 on 2024-07-01 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0010_rename_si_id_teammember_si'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='SI',
        ),
        migrations.AddField(
            model_name='teammember',
            name='si',
            field=models.CharField(max_length=10, null=True),
        ),
    ]