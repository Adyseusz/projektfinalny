# Generated by Django 3.1.5 on 2021-01-29 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza_firm', '0016_auto_20210129_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='star',
        ),
        migrations.DeleteModel(
            name='Stars',
        ),
    ]
