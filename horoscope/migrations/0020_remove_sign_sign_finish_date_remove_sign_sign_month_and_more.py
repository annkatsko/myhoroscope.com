# Generated by Django 4.1.1 on 2022-09-27 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope', '0019_remove_sign_finish_date_remove_sign_month_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sign',
            name='sign_finish_date',
        ),
        migrations.RemoveField(
            model_name='sign',
            name='sign_month',
        ),
        migrations.RemoveField(
            model_name='sign',
            name='sign_start_date',
        ),
    ]
