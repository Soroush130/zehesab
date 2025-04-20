from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator

from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, phone, first_name, last_name, password=None):
        if not phone:
            raise ValueError('شماره تلفن ضروری است')
        if not first_name:
            raise ValueError('نام ضروری است')
        if not last_name:
            raise ValueError('نام خانوادگی ضروری است')

        user = self.model(
            phone=phone,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, first_name, last_name, password=None):
        user = self.create_user(
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(
        verbose_name="شماره تلفن",
        max_length=21,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="شماره تلفن باید به فرمت صحیح وارد شود. مثال: 09123456789"
            )
        ]
    )
    first_name = models.CharField(verbose_name="نام", max_length=100)
    last_name = models.CharField(verbose_name="نام خانوادگی", max_length=100)
    is_active = models.BooleanField(verbose_name="فعال", default=True)
    is_staff = models.BooleanField(verbose_name="کارمند", default=False)
    is_superuser = models.BooleanField(verbose_name="ادمین", default=False)
    date_joined = models.DateTimeField(verbose_name="تاریخ عضویت", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="آخرین زمان لاگین", auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone})"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
