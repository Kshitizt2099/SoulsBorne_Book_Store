# Generated by Django 4.2.3 on 2023-08-12 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soulsbornestore', '0006_alter_review_score_alter_sales1_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='reviewmk1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('userid', models.TextField(max_length=10)),
                ('desc', models.TextField(max_length=100)),
                ('name', models.TextField(max_length=50)),
                ('pid', models.TextField(max_length=50)),
                ('score', models.IntegerField(default=1, null=True)),
            ],
        ),
    ]
