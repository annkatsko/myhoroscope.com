from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('learn_sign/', cache_page(60)(views.SignFormView.as_view()), name='learn-sign'),
    path('homepage/', cache_page(60)(views.SignListView.as_view()), name='main-page'),
    path('sign/', cache_page(60)(views.SignViewToUser.as_view()), name='your-sign'),
    path('<slug:slug>/', cache_page(60)(views.SignDetailView.as_view()), name='sign-detail'),
    path('<slug:slug>/<day>/', cache_page(60)(views.HoroscopeFormTemplateView.as_view()), name='horoscope')
]

