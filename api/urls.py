
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', admin.site.urls),
    url(r'^groups/', admin.site.urls),
    url(r'^input/', admin.site.urls),
]
