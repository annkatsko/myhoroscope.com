from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('horoscope/', cache_page(60)(views.get_horoscope_of_sign), name='learn-horoscope'),
    path('learn_sign/', views.learn_user_sign, name='learn-sign'),
    path('', cache_page(60)(views.SignsListView.as_view()), name='main-page'),
    path('<slug:slug>/', cache_page(60)(views.SignDetailView.as_view()), name='sign-detail'),
    path('horoscope/<slug:slug>/<day>/', cache_page(60)(views.HoroscopeTemplateView.as_view()), name='horoscope'),

]

