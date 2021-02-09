# Generated by Django 3.1.5 on 2021-02-01 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza_firm', '0021_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]