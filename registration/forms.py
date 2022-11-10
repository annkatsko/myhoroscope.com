from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from configs import settings
from registration.models import Profile
from django.contrib.auth.forms import AuthenticationForm
import re


def validate_telegram_username(val):
    if re.findall(r'[а-я]', val) or re.findall(r'[!"@#№$%,?^&.(*;)/\']', val):
        raise ValidationError('Введите валидное имя пользователя', params={'value': val})


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    username = forms.CharField(label='Имя пользователя')
    first_name = forms.CharField(label='Имя')
    email = forms.CharField(label='Адрес электронной почты')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', required=False)
    email = forms.CharField(label='Адрес электронной почты', required=False)

    class Meta:
        model = User
        fields = ('first_name', 'email')


class ProfileEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(label='Дата рождения', input_formats=settings.DATE_INPUT_FORMATS,
                                    error_messages={'invalid': 'Введите дату в правильном формате ("день.месяц.год")',
                                                    'invalid date': 'Вы ввели некорректную дату'}, required=False)
    telegram = forms.CharField(label='Имя пользователя в Телеграм', min_length=5,
                               validators=[validate_telegram_username], required=False)

    class Meta:
        model = Profile
        fields = ('date_of_birth', 'telegram', 'zodiac_sign')







class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['username'].label = 'Имя пользователя'
        self.fields['password'].label = 'Пароль'