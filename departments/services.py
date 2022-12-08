from departments.models import Department


def get_or_create_departments():
    Department.objects.all().delete()
    departments_data = [
        ('PHILOSOPHY', '1960-10-30'), ('MATHEMATICS AND NATURAL SCIENCES', '1971-01-01'), ('PHILOLOGY', '1960-01-01'),
        ('LAW', '1961-06-23'), ('ECONOMICS', '1991-09-21'), ('ELECTRICAL AND COMPUTER ENGINEERING', '1961-10-20'),
        ('MECHANICAL ENGINEERING', '1961-10-20'), ('MEDICINE', '1991-09-21'), ('ARTS', '1973-07-31'),
        ('AGRICULTURE AND VETERINARY', '1973-07-31'), ('GEOSCIENCES AND TECHNOLOGY', '1973-07-31'),
        ('EDUCATION', '1979-08-31'),
    ]

    departments = [Department(name=name.strip(), opened_on=opened_on) for name, opened_on in departments_data]
    for department in departments:
        department.save()

    return departments
