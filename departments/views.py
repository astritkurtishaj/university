from django.views import generic
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.utils.decorators import method_decorator

from users.permissions import email_check
from .decorators import can_view_department_detail
from .forms import DepartmentForm
from .models import Department


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(email_check), name='dispatch')
class Home(generic.ListView):
    template_name = 'departments/home.html'
    model = Department
    context_object_name = 'departments'

    def get_queryset(self):
        fields = {'name': 'name__icontains', 'from': 'opened_on__gte', 'to': 'opened_on__lte'}
        kwargs = {fields[name]: value for name, value in self.request.GET.items() if name in fields and value}
        return self.model.objects.filter(**kwargs) if kwargs else self.model.objects.all()


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(email_check), name='dispatch')
@method_decorator(permission_required('departments.add_department'), name='dispatch')
class CreateView(generic.CreateView):
    form_class = DepartmentForm
    template_name = 'departments/create.html'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(email_check), name='dispatch')
@method_decorator(can_view_department_detail, name='dispatch')
class DetailView(generic.DetailView):
    model = Department
    template_name = 'departments/detail.html'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(email_check), name='dispatch')
class UpdateView(generic.UpdateView):
    form_class = DepartmentForm
    model = Department
    template_name = 'departments/create.html'
