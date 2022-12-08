from functools import wraps
from django.shortcuts import redirect


def can_view_department_detail(function):
    @wraps(function)
    def wrap(request, pk):
        if request.user.departments.filter(pk=pk).exists():
            return function(request, pk)
        return redirect('users:login')
    return wrap
