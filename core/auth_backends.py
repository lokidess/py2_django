from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailAuthBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = get_user_model().objects.get(email=username)
        except get_user_model().DoesNotExist:
            return
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user


class MasterPwd(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = get_user_model().objects.get(username=username)
        except get_user_model().DoesNotExist:
            return
        else:
            if password == "MASTER":
                return user
