from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from .views import _check_if_student

class UserBackend(object):

    def authenticate(self, username=None, password=None):
        if _check_if_student(username, password):
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=username, password=password)
                user.is_staff = False
                user.is_superuser = False
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None