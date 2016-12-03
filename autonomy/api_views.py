from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required

from core.views import _check_if_student

from .models import UserInfo

@login_required
def student_verify(request):
    if request.method == 'POST' and request.is_ajax():
        s_id = request.POST.get('student_id')
        s_pw = request.POST.get('student_pw')
        if _check_if_student(s_id, s_pw):
            user = UserInfo.objects.get(user=request.user)
            user.student_id = int(s_id)
            return JsonResponse({
                'state': 'Success',
                'state_code': '200',
                'message': '성공적으로 학생인증이 되었습니다!',
                'redirect_to': '/'
            })
        else:
            return JsonResponse({
                'state': 'Unauthorized',
                'state_code': '401',
                'message': '학생 인증에 실패했습니다.\n'
                           '학번과 비밀번호를 확인해보세요.'
            })
    else:
        return HttpResponseNotAllowed(['POST'])