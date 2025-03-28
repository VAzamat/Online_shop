from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('dealer.urls',namespace='dealer')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.AdminSite.site_header = 'Моя админка'
admin.AdminSite.index_title = 'Главная страница настройки администрования приложения'
