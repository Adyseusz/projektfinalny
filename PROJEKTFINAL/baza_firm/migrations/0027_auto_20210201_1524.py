# Generated by Django 3.1.5 on 2021-02-01 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza_firm', '0026_auto_20210201_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='atribute',
        ),
        migrations.AddField(
            model_name='company',
            name='atribute',
            field=models.ManyToManyField(null=True, to='baza_firm.Atributes'),
        ),
    ]