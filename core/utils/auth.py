import random
from django.conf import settings
from django.contrib.auth import load_backend, login


def random_string(max_length=10, chars=list('abcdefghijklmnopqrstuvwxyz0123456789-')):
    min_length = 6
    if max_length < min_length:
        max_length = min_length
    length = random.randint(min_length, max_length)
    return ''.join(random.choice(chars) for i in range(length))


def instant_login(request, user):
    '''
    Log in a user without requiring credentials
    '''
    if not hasattr(user, 'backend'):
        for backend in settings.AUTHENTICATION_BACKENDS:
            if user == load_backend(backend).get_user(user.pk):
                user.backend = backend
                break
    if hasattr(user, 'backend'):
        return login(request, user)
