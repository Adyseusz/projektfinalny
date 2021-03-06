# Generated by Django 3.1.5 on 2021-01-29 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza_firm', '0007_auto_20210128_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='services',
            field=models.ManyToManyField(to='baza_firm.CategoryServices'),
        ),
        migrations.AlterField(
            model_name='categoryservices',
            name='service',
            field=models.CharField(blank=True, default='Inne', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='cities',
            field=models.ManyToManyField(to='baza_firm.City'),
        ),
    ]
