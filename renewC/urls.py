from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^api/', include('autonomy.api_urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', include('autonomy.urls')),
]
