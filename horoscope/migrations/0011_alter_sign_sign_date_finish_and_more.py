# Generated by Django 4.1.1 on 2022-09-27 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope', '0010_sign_sign_date_finish_sign_sign_date_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='sign_date_finish',
            field=models.IntegerField(default='1', null=True),
        ),
        migrations.AlterField(
            model_name='sign',
            name='sign_date_start',
            field=models.IntegerField(default='1', null=True),
        ),
    ]
