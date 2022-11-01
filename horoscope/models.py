from django.db import models


class Sign(models.Model):
    """Class for Zodiac sign models."""
    def __str__(self):
        return self.sign_name

    sign_name = models.CharField('Знак зодиака', unique=True,  help_text='Это поле для имени знака Зодиака', max_length=20)
    sign_info = models.TextField('Информация о знаке', help_text='Это поле для информации о знакае Зодиака',
                                 max_length=500)
    sign_image = models.ImageField(upload_to='sign_images', default='sign_images/libra.jpg')
    slug = models.SlugField(null=True)

