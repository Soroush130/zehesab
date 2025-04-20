from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError('شماره تلفن ضروری است')

        user = self.model(phone=phone)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password=None):
        user = self.create_user(
            phone=phone,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(verbose_name="شماره تلفن", max_length=21, unique=True)
    is_active = models.BooleanField(verbose_name="فعال", default=True)
    is_staff = models.BooleanField(verbose_name="کارمند", default=False)
    is_superuser = models.BooleanField(verbose_name="ادمین", default=False)
    data_joined = models.DateTimeField(verbose_name="تاریخ عضویت", null=True)
    last_login = models.DateTimeField(verbose_name="اخرین زمان لاگین", null=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin(self):
        return self.is_staff
