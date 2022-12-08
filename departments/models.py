from django.db import models
from django.shortcuts import reverse


class Department(models.Model):
    name = models.CharField(max_length=250)
    opened_on = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('departments:detail', args=(self.pk, ))