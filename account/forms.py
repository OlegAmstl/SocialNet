from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class LoginForm(forms.Form):
    '''
    Форма входа в аккаунт.
    '''

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Данный email уже занят.')
        return data


class UserEditForm(forms.ModelForm):
    '''
    Форма изменения данных пользователя.
    '''

    class Meta:

        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Данный email уже занят.')
        return data


class ProfileEditForm(forms.ModelForm):
    '''
    Форма редактирования профиля.
    '''

    class Meta:

        model = Profile
        fields = ['date_of_birth', 'photo']

