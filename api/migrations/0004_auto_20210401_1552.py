# Generated by Django 3.1.7 on 2021-04-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_command'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='drone_name',
            field=models.CharField(max_length=20),
        ),
    ]
