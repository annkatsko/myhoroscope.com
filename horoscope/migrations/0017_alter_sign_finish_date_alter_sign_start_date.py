# Generated by Django 4.1.1 on 2022-09-27 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope', '0016_alter_sign_finish_date_alter_sign_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='finish_date',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='sign',
            name='start_date',
            field=models.IntegerField(default=1),
        ),
    ]
