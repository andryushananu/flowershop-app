# Generated by Django 3.0 on 2020-06-29 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flori', '0003_auto_20200629_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produse',
            name='pret_cumparare',
            field=models.FloatField(),
        ),
    ]
