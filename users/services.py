from django.contrib.auth.models import Group, Permission

from departments.models import Department
from users.models import User


def create_users():
    User.objects.all().delete()
    ardit = User.create_user(email='ardit@uni-edu.pr', password='ardit123')
    abetare = User.create_user(email='abetare@uni-edu.pr', password='abetare123')
    bajram = User.create_user(email='bajram@uni-edu.pr', password='bajram123')
    return ardit, abetare, bajram


def create_groups():
    Group.objects.all().delete()
    Group.objects.bulk_create([Group(name='Rector'), Group(name='Dean'), Group(name='Professor')])


def assign_groups():
    User.objects.get(email='ardit@uni-edu.pr').groups.set([Group.objects.get(name='Rector')])
    User.objects.get(email='abetare@uni-edu.pr').groups.set([Group.objects.get(name='Dean')])
    User.objects.get(email='bajram@uni-edu.pr').groups.set([Group.objects.get(name='Professor')])


def assign_permissions_to_groups():
    add_department = Permission.objects.get(codename='add_department')
    view_students = Permission.objects.get(codename='view_students')
    add_student = Permission.objects.get(codename='add_student')

    Group.objects.get(name='Rector').permissions.set([add_department, view_students, add_student])
    Group.objects.get(name='Dean').permissions.set([view_students, add_student])


def assign_users_to_departments():
    ardit = User.objects.get(email='ardit@uni-edu.pr')
    abetare = User.objects.get(email='abetare@uni-edu.pr')
    bajram = User.objects.get(email='bajram@uni-edu.pr')

    ardit.departments.set(Department.objects.filter(name__in=['PHILOSOPHY', 'PHILOLOGY']))
    abetare.departments.set(Department.objects.filter(name__in=['LAW', 'ECONOMICS']))
    bajram.departments.set(Department.objects.filter(name__in=['ARTS', 'EDUCATION']))

