# Generated by Django 3.1.5 on 2021-02-02 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza_firm', '0031_auto_20210202_1905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='atribute',
            new_name='atribute_comp',
        ),
    ]
