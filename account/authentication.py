from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class EmailAuthBackend:
    '''
    Аутентифицировать по средствам электронной почты.
    '''

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


def create_profile(backend, user, *args, **kwargs):
    '''
    Создать профиль пользователя для социальной аутентификации.
    '''
    Profile.objects.get_or_create(user=user)
