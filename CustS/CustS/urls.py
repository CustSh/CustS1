
from django.conf.urls import handler404
from django.contrib import admin
from django.template.context_processors import request
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('catalog/',include('catalog.urls')),
    path('users/', include('users.urls')),
    path('carts/', include('carts.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
