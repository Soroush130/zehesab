from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, ContactUs


class CustomUserAdmin(UserAdmin):
    list_display = ('phone', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('phone', 'first_name', 'last_name')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('اطلاعات شخصی', {'fields': ('first_name', 'last_name', 'role', 'profile_image')}),
        ('دسترسی‌ها', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("phone", 'priority')



admin.site.register(User, CustomUserAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
