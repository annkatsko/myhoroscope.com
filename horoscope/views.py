from configs.constants import days, signs_slugs, zodiac_signs_list
from django.shortcuts import render
from django.views import generic
from .models import Sign
from .horoscope_parcer import parcer
from .forms import SignForm, HoroscopeForm
from django.shortcuts import redirect


def _define_sign(day: int, month: int) -> str:
    """
    Return the Zodiac sign according to day and month.

    :param day: Date of Birth.
    :param month: Month of Birth.
    :return: Zodiac sign
    """

    days_variants = (20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 23, 22)
    month -= 1
    if day > days_variants[month]:
        sign = zodiac_signs_list[month]
    else:
        sign = zodiac_signs_list[month - 1]
    return sign


class SignViewToUser(generic.TemplateView):
    """Render a template of user's Zodiac sign after submitting SignForm."""

    def get(self, request, *args, **kwargs):
        """Return rendered template of user's Zodiac sign with context."""
        day = int(request.GET['birthday_day'])
        month = int(request.GET['birthday_month'])
        sign = _define_sign(day, month)
        context = {'button_slug': signs_slugs[sign],
                   'sign_list': Sign.objects.all(), 'sign': sign}
        return render(request, "horoscope/show_sign.html", context=context)


class SignsListView(generic.ListView):
    """Render list of Zodiac sign objects."""

    model = Sign
    template_name = 'horoscope/home_page.html'


class SignDetailView(generic.DetailView):
    """Render a "detail" view of Zodiac sign object."""

    model = Sign

    def get_context_data(self, **kwargs):
        """Add list of signs to context."""
        context = super().get_context_data(**kwargs)
        context['sign_list'] = Sign.objects.all()
        return context


class SignFormView(generic.FormView):
    """
    A view for displaying a form for learning Zodiac sign
    and rendering a template response.
    """

    form_class = SignForm
    template_name = 'horoscope/learn_sign.html'
    initial = {'birthday_day': '01',
               'birthday_month': '01'}

    def get_context_data(self, **kwargs):
        """Add list of signs to context."""
        context = super().get_context_data(**kwargs)
        context['sign_list'] = Sign.objects.all()
        return context


class HoroscopeTemplateView(generic.TemplateView):
    """
    Render a template of a horoscope.
    Pass keyword arguments from the URLconf to the context.
    """

    template_name = 'horoscope/horoscope_page.html'

    def get(self, request, *args, **kwargs):
        """Return rendered template of a horoscope with context."""
        horoscope_text = parcer.get_daily_horoscope(some_sign=kwargs['slug'],
                                                    day=kwargs['day'])

        return render(request, 'horoscope/horoscope_page.html',
                      context={'horoscope': horoscope_text,
                               'sign_list': Sign.objects.all(),
                               'day': days[kwargs['day']],
                               'slug_day': kwargs['day'],
                               'sign': kwargs['slug']}
                               )


def get_horoscope_of_sign(request):
    if request.method == 'GET':
        form = HoroscopeForm(request.GET)

        if form.is_valid():
            day = form.cleaned_data['day']
            sign = form.cleaned_data['zodiac_sign']
            return redirect(f'/horoscope/{sign}/{day}')
    else:
        form = HoroscopeForm()

    return render(request, 'horoscope/get_horoscope.html', {'form': form, 'sign_list': Sign.objects.all(),})
