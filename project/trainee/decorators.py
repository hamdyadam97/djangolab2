from django.core.exceptions import PermissionDenied
from .models import *
import time, datetime
import math
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test

def the_time(function):
    def wrap(request, *args, **kwargs):
        if datetime.datetime.now().hour < 11:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def logout_required(function=None, logout_url=settings.LOGOUT_URL):
    actual_decorator = user_passes_test(
        lambda u: not u.is_authenticated,
        login_url=logout_url
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

