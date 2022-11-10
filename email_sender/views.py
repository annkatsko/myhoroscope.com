from configs.constants import days
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from horoscope.horoscope_parcer.parcer import get_daily_horoscope
from django.core.mail import send_mail
from horoscope.models import Sign
from.forms import EmailForm


class SignFormView(generic.FormView):
    """
    A view for displaying a form for learning Zodiac sign
    and rendering a template response.
    """

    form_class = EmailForm
    template_name = 'email_sender/email_sender.html'

    def get_context_data(self, **kwargs):
        """Add list of signs to context."""
        context = super().get_context_data(**kwargs)
        context['sign_list'] = Sign.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        email_form = EmailForm(data=request.POST)
        if email_form.is_valid():
            sign = self.kwargs.get('slug')
            day = self.kwargs.get('day')
            email = request.POST.get('email')
            today_horoscope = get_daily_horoscope(some_sign=sign, day=day)
            try:
                send_mail(from_email='horoscope@gmail.com', subject=f'Твой гороскоп на {days[day]}',
                          recipient_list=[email],
                          message=today_horoscope)
                messages.success(request, message=f'Гороскоп отправлена на почту {email}.')

            except:
                messages.error(request, message="Не удалось отправить гороскоп.")

            next_url = request.POST.get('next', '/')
            return HttpResponseRedirect(next_url)

        email_form = EmailForm()

        return render(request, "email_sender/email_sender.html", {'form': email_form})
