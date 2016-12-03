from django.conf.urls import url

from .api_views import student_verify


urlpatterns = [
    url(r'^auth/$', student_verify, name='auth'),

]