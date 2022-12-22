from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView

from .forms import CreateUserForm, UserAuthenticationForm, UserEditForm, ProfileEditForm, MyPasswordChangeForm


def home(request):
    return render(request, 'users/home.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Аккаунт ' + user + ' успешно зарегистрирован!')
            return redirect('user_login')
    context = {'form': form}
    return render(request, 'users/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_profile', request.user.username)
        else:
            messages.info(request, 'Неверное имя пользователя или пароль!')
    else:
        form = UserAuthenticationForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')


class ProfileView(DetailView):
    model = User
    slug_field = 'username'
    template_name = "users/profile.html"


@login_required
def profile_edit(request):
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user_profile', request.user.username)
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'users/settings.html', context)


class MyPasswordChangeView(PasswordChangeView):
    form_class = MyPasswordChangeForm
    template_name = "users/password-change.html"
    success_url = reverse_lazy('password_reset_done_not_email')


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = "users/password-reset-done_not_email.html"
