from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'} ),
    )
    email = forms.EmailField(
        label =  'ایمیل',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
        required=True,

    )
    password = forms.CharField(
        label = 'کلمه عبور',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'کلمه عبور' }),
        required=True
    )
    confirm_password = forms.CharField(
        label = 'کلمه عبور',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'تکرار کلمه عبور'}),
        required=True
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه ی عبور با تکرار آن مغایرت دارد..!')


class CompleteRegistrationForm(forms.Form):
    first_name = forms.CharField(
        label='نام',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'val-username',
                   'for': 'val-username','name': "val-username" , 'value' : 'Siavash'})
    )
    last_name = forms.CharField(
        label=  'نام خانوادگی',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'val-username',
                   'for': 'val-username','name': "val-username", 'value' : 'rad'})
    )
    birthday = forms.DateField(
        label=  'تاریخ تولد',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'val-username',
                   'for': 'val-username','name': "val-username",'value' : '12-11-1379' })
    )
    gender = forms.IntegerField(
        label=  'جنسیت',
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'id': 'val-username',
                   'for': 'val-username','name': "val-username",'value' : 'مرد' })
    )
    national_id = forms.IntegerField(
        label=  'کدملی',
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'id': 'val-username',
                   'for': 'val-username','name': "val-username",'value' : '۴۰۶۱۲۱۰۵۶۴' })
    )
    phone_number = forms.IntegerField(
        label=  'شماره همراه',
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'id': 'val-username',
                   'for': 'val-username','name': "val-username", 'value' : '۰۹۳۶۰۵۸۱۰۲۰' })
    )

class LoginForm(forms.Form):
    email = forms.EmailField(
        # label =  'ایمیل',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل', 'autocomplete': 'off'}),
        required=True,

    )
    password = forms.CharField(
        # label = 'کلمه عبور',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'کلمه عبور', 'autocomplete': 'off'}),
        required=True
    )


