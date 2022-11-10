from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('horoscope/', cache_page(60)(views.get_horoscope_of_sign), name='learn-horoscope'),
    path('learn_sign/', cache_page(60)(views.SignFormView.as_view()), name='learn-sign'),
    path('homepage/', cache_page(60)(views.SignsListView.as_view()), name='main-page'),
    path('sign/', cache_page(60)(views.SignViewToUser.as_view()), name='your-sign'),
    path('<slug:slug>/', cache_page(60)(views.SignDetailView.as_view()), name='sign-detail'),
    path('<slug:slug>/<day>/', cache_page(60)(views.HoroscopeTemplateView.as_view()), name='horoscope'),

]

