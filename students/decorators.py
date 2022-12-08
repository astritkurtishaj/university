from functools import wraps
from django.shortcuts import redirect

from .models import Student


def can_view_student_detail(function):
    @wraps(function)
    def wrap(request, pk):
        student = Student.objects.get(pk=pk)
        if request.user.departments.filter(pk=student.department.pk).exists():
            return function(request, pk)
        return redirect('users:login')
    return wrap
