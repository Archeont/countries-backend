# Generated by Django 3.0.10 on 2022-10-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_viewer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='gdp',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]