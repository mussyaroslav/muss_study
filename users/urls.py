from django.urls import path
from .views import *

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('settings/', profile_edit, name='profile_edit'),
    path('password-reset/', auth_views.PasswordResetView.as_view
         (template_name='users/password-reset.html'),
         name='password_reset'),
    path('password-reset-sent/', auth_views.PasswordResetDoneView.as_view
         (template_name='users/password-reset-sent.html'),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view
         (template_name='users/password-reset-form.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view
         (template_name='users/password-reset-complete.html'),
         name='password_reset_complete'),
    path('settings/password-change/', MyPasswordChangeView.as_view(), name='password_change'),
    path('settings/password-change/done/', MyPasswordResetDoneView.as_view(), name='password_reset_done_not_email'),
    path('<str:slug>/', ProfileView.as_view(), name='user_profile'),
    path('', home, name='home')
]
