from django import forms


class SignForm(forms.Form):
    CHOICES =[('1', 'Январь'),
              ('2', 'Февраль'),
              ('3', 'Март'),
              ('4', 'Апрель'),
              ('5', 'Май'),
              ('6', 'Июнь'),
              ('7', 'Июль'),
              ('8', 'Август'),
              ('9', 'Сентябрь'),
              ('10', 'Октябрь'),
              ('11', 'Ноябрь'),
              ('12', 'Декабрь')]

    birthday_day = forms.IntegerField(label="Ваша дата", required=True, min_value=1, max_value=31,
                                          error_messages={'max_value': 'В месяце максимум 31 день',
                                                          'min_value': 'Месяц начинается с 1-го числа'})
    birthday_month = forms.ChoiceField(choices=CHOICES, label="Ваш месяц", required=True,
                                       error_messages={'choices': 'Выберите правильный месяц.'})


class HoroscopeForm(forms.Form):
    SIGNS = (
        ('aries', 'Овен'),
        ('taurus', 'Телец'),
        ('gemini', 'Близнецы'),
        ('cancer', 'Рак'),
        ('leo', 'Лев'),
        ('virgo', 'Дева'),
        ('libra', 'Весы'),
        ('scorpio', 'Скорпион'),
        ('sagittarius', 'Стрелец'),
        ('capricorn', 'Козерог'),
        ('aquarius', 'Водолей'),
        ('pisces', 'Рыбы'),
    )

    DAYS = (
        ('yesterday', 'Вчера'),
        ('today', 'Сегодня'),
        ('tomorrow', 'Завтра'),
        ('month', 'Месяц'),
    )

    zodiac_sign = forms.ChoiceField(label='Знак зодиака', required=True, choices=SIGNS)
    day = forms.ChoiceField(label='Период', required=True, choices=DAYS)
