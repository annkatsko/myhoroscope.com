
# Generated by Django 4.1.1 on 2022-10-02 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope', '0023_remove_sign_sign_finish_date_remove_sign_sign_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='sign_info',
            field=models.TextField(help_text='Это поле для информации о знакае Зодиака', max_length=500, verbose_name='Информация о знаке'),
        ),
    ]
