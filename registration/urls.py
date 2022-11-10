from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from registration import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView


urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('register/', views.register, name='registration'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit/', views.edit, name='edit'),
    path('password-reset/', PasswordResetView.as_view(
        template_name='registration/my_password_reset.html',
        email_template_name='registration/my_password_reset_email.html',
        subject_template_name='registration/my_password_reset_subject.txt'), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name="registration/my_password_reset_done.html"), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='registration/my_password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(
        template_name='registration/my_password_reset_complete.html'), name='password_reset_complete'),
    ]