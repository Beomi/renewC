from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required

from core.views import _check_if_student

from .models import UserInfo
