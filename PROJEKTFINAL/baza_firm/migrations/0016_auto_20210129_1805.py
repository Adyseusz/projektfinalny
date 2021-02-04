# Generated by Django 3.1.5 on 2021-01-29 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baza_firm', '0015_auto_20210129_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='comments',
            name='star',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='baza_firm.stars'),
        ),
    ]
