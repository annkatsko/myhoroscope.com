# Generated by Django 4.1.1 on 2022-09-27 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope', '0012_remove_sign_sign_date_finish_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sign',
            name='sign_date_finish',
            field=models.IntegerField(default='31', max_length='2'),
        ),
        migrations.AddField(
            model_name='sign',
            name='sign_date_start',
            field=models.IntegerField(default='1', max_length='2'),
        ),
    ]
