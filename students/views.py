from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required


from departments.models import Department
from users.permissions import email_check
from .decorators import can_view_student_detail
from .forms import StudentForm
from .models import Student


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(email_check), name='dispatch')
@method_decorator(permission_required('students.view_students'), name='dispatch')
class HomeView(generic.ListView):
    model = Student
    template_name = 'students/home.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        return context

    def get_queryset(self):
        fields = {'first_name': 'first_name__icontains', 'last_name': 'last_name__icontains', 'department': 'department__id'}
        kwargs = {fields[name]: value for name, value in self.request.GET.items() if name in fields and value}
        return self.model.objects.filter(**kwargs) if kwargs else self.model.objects.all()


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(email_check), name='dispatch')
@method_decorator(permission_required('students.add_student'), name='dispatch')
class CreateView(generic.CreateView):
    form_class = StudentForm
    template_name = 'students/create.html'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(email_check), name='dispatch')
@method_decorator(can_view_student_detail, name='dispatch')
class DetailView(generic.DetailView):
    model = Student
    template_name = 'students/detail.html'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(email_check), name='dispatch')
class UpdateView(generic.UpdateView):
    form_class = StudentForm
    model = Student
    template_name = 'students/create.html'

