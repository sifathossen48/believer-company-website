# Generated by Django 4.2 on 2024-05-13 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GetQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('eamil', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('message', models.TextField()),
            ],
        ),
    ]
