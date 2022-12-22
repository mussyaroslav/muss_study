from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User

from users.models import Profile


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField,
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password__input'}))

    def __init__(self, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'username__input'})


class CreateUserForm(UserCreationForm):
    username = forms.CharField(required=True, min_length=6, max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'register__input'}),
            'first_name': forms.TextInput(attrs={'class': 'first__name__input'}),
            'last_name': forms.TextInput(attrs={'class': 'first__name__input'})
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'register__input'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'register__input'})
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'register__input'})

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с таким именем уже существует.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Пользователь с таким почтовым адресом уже зарегистрирован.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароли не совпадают.')
        return password2


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'settings__input'}),
            'first_name': forms.TextInput(attrs={'class': 'settings__input'}),
            'last_name': forms.TextInput(attrs={'class': 'settings__input'})
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo', 'photo_background', 'city', 'school',  'vk_link', 'inst_link')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'settings__input'}),
            'city': forms.TextInput(attrs={'class': 'settings__input'}),
            'school': forms.TextInput(attrs={'class': 'settings__input'}),
            'vk_link': forms.TextInput(attrs={'class': 'settings__input'}),
            'inst_link': forms.TextInput(attrs={'class': 'settings__input'}),
        }


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'new_password_input',
                                                                     'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'new_password_input',
                                                                      'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'new_password_input',
                                                                      'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

