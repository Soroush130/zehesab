from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User, ContactUs


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('phone',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('phone',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label='نام',
        widget=forms.TextInput(attrs={'placeholder': 'نام خود را وارد کنید'})
    )
    last_name = forms.CharField(
        label='نام خانوادگی',
        widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی خود را وارد کنید'})
    )
    phone = forms.CharField(
        label='شماره تلفن',
        widget=forms.TextInput(attrs={'placeholder': 'شماره تلفن خود را وارد کنید'})
    )
    password1 = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور خود را وارد کنید'})
    )
    password2 = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور را مجدداً وارد کنید'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'password1', 'password2']


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['phone', 'title', 'description', 'priority']


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_image']