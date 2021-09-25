# Generated by Django 3.1.7 on 2021-08-05 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_drone_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drone',
            name='owner',
        ),
        migrations.AddField(
            model_name='drone',
            name='owner_token',
            field=models.CharField(default='none', max_length=2000),
        ),
    ]
