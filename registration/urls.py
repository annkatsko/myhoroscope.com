from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from registration import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', views.register, name='registration'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit/', views.edit, name='edit'),
    # path('password-reset/', PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name='password_reset'),
    # path('password-reset/done/', PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    # path('reset/done/', PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name='password_reset_complete'),
]