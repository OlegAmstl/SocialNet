from django import forms


class LoginForm(forms.Form):
    '''
    Форма входа в аккаунт.
    '''

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)