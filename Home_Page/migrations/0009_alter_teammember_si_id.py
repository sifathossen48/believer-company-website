# Generated by Django 4.2 on 2024-07-01 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0008_alter_teammember_si_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='SI_ID',
            field=models.CharField(max_length=10),
        ),
    ]
