import requests

def _check_if_student(user_id, user_pw):
    payload = {
        'usr_id': str(user_id),
        'usr_pwd': str(user_pw)
    }
    with requests.Session() as s:
        s.post('http://lms.snue.ac.kr/ilos/lo/login.acl', data=payload)
        auth = s.get('http://lms.snue.ac.kr/ilos/main/main_form.acl', allow_redirects=False)
        authed_text = '<div class="quick-item-text">마이페이지</div>'
        if authed_text in auth.text:
            result = True
        else:
            result = False
        return result