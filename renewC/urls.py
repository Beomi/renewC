from django.conf.urls import url, include, static
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^api/', include('autonomy.api_urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', include('autonomy.urls')),
]
urlpatterns += static.static('/files/',) # document_root=settings.MEDIA_ROOT)
