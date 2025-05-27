from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from .views import home, contact_us, about_us
from blogs.views import upload_image
from blogs.sitemaps import BlogSitemap

sitemaps_dict = {
    'blogs': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('contact_us/', contact_us, name='contact_us'),
    path('about_us/', about_us, name='about_us'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('blogs/', include('blogs.urls'), name='blogs'),
    path('upload_image/', upload_image, name='upload_image'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps_dict}, name='sitemap'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
