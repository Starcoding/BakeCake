from django import forms
from .models import CustomUser
from phonenumber_field.formfields import PhoneNumberField


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя')
    second_name = forms.CharField(label='Фамилия')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    social_id = forms.CharField(label='Соц. сети')
    address = forms.CharField(label='Адрес доставки')
    phone_number = PhoneNumberField(label='Номер телефона')


    class Meta:
        model = CustomUser
        fields = ('username',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']