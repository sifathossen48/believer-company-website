# Generated by Django 4.2 on 2024-07-01 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0011_remove_teammember_si_teammember_si'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='is_Draft',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='si',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
