from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.shortcuts import redirect


def not_required_login(view_func):
    """
    A decorator to allow access to the view for both authenticated and non-authenticated users.
    """
    def _wrapped_view(request, *args, **kwargs):
        # If the user is authenticated, we pass the request as is
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return _wrapped_view
