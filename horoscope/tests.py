import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "configs.settings")

import django
django.setup()

from django.core.management import call_command

from django.test import TestCase, SimpleTestCase

from horoscope.models import Sign
from django import forms
import unittest
from horoscope.views import define_sign



class SignModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.actor = Sign.objects.create(
            sign_name="Test_Sign",
            sign_info="some_info.....",
            sign_image='media/sign_images/libra.jpg',
            slug='some_slug'
        )

    def test_sign_name_label(self):
        sign = Sign.objects.get(id=1)
        field_label = sign._meta.get_field('sign_name').verbose_name
        self.assertEquals(field_label, 'Знак зодиака')

    def test_sign_info_label(self):
        sign = Sign.objects.get(id=1)
        field_label = sign._meta.get_field('sign_info').verbose_name
        self.assertEquals(field_label, 'Информация о знаке')

    def test_sign_name_max_length(self):
        sign=Sign.objects.get(id=1)
        max_length = sign._meta.get_field('sign_name').max_length
        self.assertEquals(max_length, 20)

    def test_sign_info_max_length(self):
        sign = Sign.objects.get(id=1)
        max_length = sign._meta.get_field('sign_info').max_length
        self.assertEquals(max_length, 500)


class SignFormTest(SimpleTestCase):
    def test_sign_form(self):
        self.assertFieldOutput(forms.IntegerField, {'1': 1}, {'aaa': ['Enter a whole number.']}, empty_value=None)




class HoroscopeTestCase(unittest.TestCase):
    def test_define_sign(self):
        sign = define_sign(19, 10)
        self.assertEqual('Весы', sign)
        self.assertIsInstance(sign, str)