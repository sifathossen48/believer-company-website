# Generated by Django 4.2 on 2024-05-12 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='why_selecting_us',
            name='custom_Services_Title',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='why_selecting_us',
            name='happy_Clients_Title',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='why_selecting_us',
            name='personal_Consultants_Title',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='why_selecting_us',
            name='years_of_Experience_Title',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
