from django.urls import path
from . import views






urlpatterns = [
    path('learn_sign/', views.SignFormView.as_view(), name='learn-sign'),
    path('', views.SignListView.as_view(), name='main-page'),
    path('sign/', views.SignViewToUser.as_view(), name='your-sign'),
    path('<slug:slug>/', views.SignDetailView.as_view(), name='sign-detail'),
    path('<slug:slug>/<day>/', views.HoroscopeFormTemplateView.as_view(), name='horoscope')
]
