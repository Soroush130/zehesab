# Generated by Django 5.2 on 2025-04-23 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_profile_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'ordering': ['priority'], 'verbose_name': 'تماس با ما', 'verbose_name_plural': 'تماس با ما'},
        ),
    ]
