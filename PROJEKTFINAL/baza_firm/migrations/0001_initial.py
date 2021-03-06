# Generated by Django 3.1.5 on 2021-01-26 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=500)),
                ('services', models.TextField(max_length=500)),
                ('contact', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=9)),
                ('only_in_net', models.BooleanField(default=False)),
                ('adress', models.TextField(max_length=250)),
                ('nip', models.IntegerField(max_length=15)),
            ],
        ),
    ]
