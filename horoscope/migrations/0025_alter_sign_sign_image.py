# Generated by Django 4.1.1 on 2022-11-01 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope', '0024_alter_sign_sign_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='sign_image',
            field=models.ImageField(default='sign_images/libra.jpg', upload_to='horoscope/sign_images'),
        ),
    ]
