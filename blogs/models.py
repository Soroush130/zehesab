from django.db import models
from accounts.models import User
from django.utils.text import slugify


class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft', 'پیش‌نویس'),
        ('published', 'منتشر شده'),
    )

    title = models.CharField(max_length=255, verbose_name="عنوان")
    slug = models.SlugField(unique=True, blank=True, verbose_name="نامک (slug)")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده")
    content = models.TextField(verbose_name="محتوا")
    excerpt = models.TextField(blank=True, null=True, verbose_name="خلاصه")
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True, verbose_name="تصویر شاخص")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="وضعیت")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")
    published_at = models.DateTimeField(null=True, blank=True, verbose_name="تاریخ انتشار")

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
