# Generated by Django 4.1.1 on 2022-11-06 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_alter_profile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]