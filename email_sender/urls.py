from django.urls import path

from email_sender import views

urlpatterns = [
    path('emailer/<slug:slug>/<day>/', views.SignFormView.as_view(), name='send_horoscope')
]
