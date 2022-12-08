from django.db import models
from django.shortcuts import reverse

from departments.models import Department


class Student(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    department = models.ForeignKey(to=Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('students:detail', args=(self.pk, ))
