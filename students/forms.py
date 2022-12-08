from django.forms import ModelForm

from .models import Student


class StudentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for name in 'first_name', 'last_name', 'department':
            self.fields[name].widget.attrs.update({'style': 'width: 250px'})

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'department']
