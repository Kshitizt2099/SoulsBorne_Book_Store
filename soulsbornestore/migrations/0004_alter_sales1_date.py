# Generated by Django 4.2.3 on 2023-08-11 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soulsbornestore', '0003_sales1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales1',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
