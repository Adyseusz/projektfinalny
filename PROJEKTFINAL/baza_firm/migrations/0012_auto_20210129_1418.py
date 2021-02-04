# Generated by Django 3.1.5 on 2021-01-29 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baza_firm', '0011_auto_20210129_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='cities',
        ),
        migrations.RemoveField(
            model_name='company',
            name='services',
        ),
        migrations.AddField(
            model_name='categoryservices',
            name='companies',
            field=models.ManyToManyField(to='baza_firm.Company'),
        ),
        migrations.AlterField(
            model_name='categoryservices',
            name='service',
            field=models.FloatField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, default='Inne', max_length=500, null=True)),
                ('star', models.FloatField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baza_firm.company')),
            ],
        ),
    ]
