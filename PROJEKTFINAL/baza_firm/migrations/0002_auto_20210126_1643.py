# Generated by Django 3.1.5 on 2021-01-26 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza_firm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='nip',
            field=models.IntegerField(),
        ),
    ]
