# Generated by Django 3.1.5 on 2021-01-29 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza_firm', '0008_auto_20210129_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryservices',
            name='service',
            field=models.CharField(max_length=255),
        ),
    ]
