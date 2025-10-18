
from django.contrib import admin
from django.urls import path

from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nova.urls')),  # ← routes de notre app
   
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()  # Pour servir les fichiers static (CSS, JS) en dev
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Pour servir les médias (images) en dev
