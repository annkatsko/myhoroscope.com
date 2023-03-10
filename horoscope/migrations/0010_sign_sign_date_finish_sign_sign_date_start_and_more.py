# Generated by Django 4.1.1 on 2022-09-27 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope', '0009_sign_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='sign',
            name='sign_date_finish',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='sign',
            name='sign_date_start',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='sign',
            name='sign_month',
            field=models.CharField(default='1', max_length=20, unique=True, verbose_name='месяц'),
        ),
    ]
