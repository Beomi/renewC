from django.conf.urls import url

from . import api_views as api

urlpatterns = [
    url(r'^auth/$', api.user_info, name='user_info'),

]