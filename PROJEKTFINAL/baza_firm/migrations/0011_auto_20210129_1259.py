# Generated by Django 3.1.5 on 2021-01-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza_firm', '0010_auto_20210129_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='cities',
        ),
        migrations.AddField(
            model_name='company',
            name='cities',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
