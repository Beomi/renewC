from django.conf.urls import url, include

# views
from .views import index


urlpatterns = [
    url(r'^$', index, name='index'),
]