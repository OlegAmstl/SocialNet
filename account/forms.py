from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    '''
    Форма входа в аккаунт.
    '''

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    '''
    Форма регистрации нового пользователя.
    '''

    password = forms.CharField(widget=forms.PasswordInput,
                               label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label='Повторите пароль')

    class Meta:

        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password(self):
        '''
        Проверка на соответствие паролей.
        '''
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']
