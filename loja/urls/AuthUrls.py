from django.urls import path
from loja.views.AuthView import login_view, register_view, logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login", login_view, name='login'),
    path("register", register_view, name='register'),
    path("logout", logout_view, name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name="auth/password_reset.html",
        email_template_name="auth/password_reset_email.html",
        subject_template_name="auth/password_reset_subject.txt"), name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="auth/password_reset_done.html"),
         name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="auth/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('password_reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="auth/password_reset_complete.html"),
         name='password_reset_complete'),
]