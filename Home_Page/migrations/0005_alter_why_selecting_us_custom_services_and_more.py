# Generated by Django 4.2 on 2024-05-14 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0004_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='why_selecting_us',
            name='custom_Services',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='why_selecting_us',
            name='happy_Clients',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='why_selecting_us',
            name='personal_Consultants',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='why_selecting_us',
            name='years_of_Experience',
            field=models.IntegerField(),
        ),
    ]
