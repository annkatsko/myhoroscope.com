# Generated by Django 4.1.1 on 2022-09-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope', '0004_alter_sign_sign_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='sign_image',
            field=models.ImageField(upload_to='sign_images'),
        ),
    ]
