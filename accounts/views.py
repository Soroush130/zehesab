from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.validators import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

import re

from accounts.forms import LoginForm, ProfileImageForm
from accounts.models import User

@login_required
def edit_profile_image(request):
    profile = request.user

    if request.method == 'POST':
        form = ProfileImageForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileImageForm(instance=profile)

    return render(request, 'accounts/edit_profile_image.html', {'form': form})

def profile(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user': user})


def login_user(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                pass
    else:
        login_form = LoginForm()

    context = {
        'login_form': login_form,
    }
    return render(request, 'accounts/login.html', context)


def register_user(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        errors = {}
        if not first_name:
            errors['firstname'] = 'نام الزامی است'
        if not last_name:
            errors['lastname'] = 'نام خانوادگی الزامی است'
        if not phone:
            errors['phone'] = 'شماره تلفن الزامی است'
        elif not re.match(r'^\+?1?\d{9,15}$', phone):
            errors['phone'] = 'شماره تلفن معتبر نیست'
        if not password or len(password) < 8:
            errors['password'] = 'رمز عبور باید حداقل 8 کاراکتر باشد'
        if not re_password:
            errors['re_password'] = 'تکرار رمز عبور را وارد کنید'
        if password != re_password:
            errors['re_password'] = 'رمز عبور مغایرت دارد'

        try:
            if User.objects.filter(phone=phone).exists():
                errors['phone'] = 'این شماره تلفن قبلاً ثبت شده است'
        except ObjectDoesNotExist:
            pass

        if errors:
            for field, error in errors.items():
                messages.error(request, error)
            return render(request, 'accounts/register.html', {
                'firstname': first_name,
                'lastname': last_name,
                'phone': phone,
            })

        try:
            user = User.objects.create_user(
                phone=phone,
                first_name=first_name,
                last_name=last_name,
                password=password
            )

            login(request, user)
            messages.success(request, 'ثبت نام با موفقیت انجام شد! خوش آمدید.')
            return redirect('home')  # تغییر از '' به 'home'

        except ValidationError as e:
            messages.error(request, f"خطا در ثبت نام: {e}")
            return render(request, 'accounts/register.html', {
                'firstname': first_name,
                'lastname': last_name,
                'phone': phone,
            })

    return render(request, 'accounts/register.html')


def log_out(request):
    logout(request)
    # messages.success(request, "با موافقیت خارج شدید")
    return redirect('accounts:login')