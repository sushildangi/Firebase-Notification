from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^push/', include('pushnotification.urls')),
    url(r'fcm/', include('fcm.urls')),
    url(r'^admin/', admin.site.urls),
]
