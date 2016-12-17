from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


from .views import _check_if_student


class UserBackend(object):

    def authenticate(self, username=None, password=None):
        UserModel = get_user_model()
        if _check_if_student(username, password):
            try:
                user = UserModel._default_manager.get_by_natural_key(username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = UserModel(username=username)
                user.is_staff = False
                user.is_superuser = False
                user.set_password(password)
                user.save()
            return user
        else:
            try:
                user = UserModel._default_manager.get_by_natural_key(username)
                if user.check_password(password) and self.user_can_authenticate(user):
                    return user
            except:
                return None


    def user_can_authenticate(self, user):
        """
        Reject users with is_active=False. Custom user models that don't have
        that attribute are allowed.
        """
        is_active = getattr(user, 'is_active', None)
        return is_active or is_active is None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None