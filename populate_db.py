import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'universitycbv.settings')
django.setup()

from departments.services import get_or_create_departments
from students.services import get_or_create_students, create_permissions as create_student_permissions
from users.services import *

get_or_create_departments()
get_or_create_students()
create_users()
create_groups()
assign_groups()
create_student_permissions()
assign_permissions_to_groups()
assign_users_to_departments()
