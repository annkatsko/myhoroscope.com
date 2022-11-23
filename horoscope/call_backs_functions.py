from horoscope.models import Sign
from horoscope.horoscope_parcer import parcer


def write_horoscope_to_database(sender, **kwargs):
    signs_objects = Sign.objects.all()
    for sign_obj in signs_objects:
        sign_obj.sign_horoscope_today = parcer.get_daily_horoscope(some_sign=sign_obj.slug)
        sign_obj.save()

