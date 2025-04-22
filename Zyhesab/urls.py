from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import home, contact_us, about_us

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('contact_us/', contact_us, name='contact_us'),
    path('about_us/', about_us, name='about_us'),
    path('accounts/', include('accounts.urls'), name='accounts'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
