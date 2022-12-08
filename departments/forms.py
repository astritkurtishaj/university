from django import forms

from .models import Department


class DepartmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        self.fields['opened_on'].widget.input_type = 'date'
        self.fields['name'].widget.attrs.update({'style': 'width: 250px'})
        self.fields['opened_on'].widget.attrs.update({'style': 'width: 250px'})

    class Meta:
        model = Department
        fields = ['name', 'opened_on']
