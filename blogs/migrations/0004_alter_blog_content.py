# Generated by Django 5.2 on 2025-04-25 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_blog_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.JSONField(verbose_name='محتوای ساختاریافته'),
        ),
    ]
