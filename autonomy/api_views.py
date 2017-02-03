from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required

from .models import UserInfo


@login_required
def user_info(request):
    info =  UserInfo.objects.get(user=request.user)
    return JsonResponse({
        'data': info
    })