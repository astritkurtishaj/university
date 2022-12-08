from django.urls import path, include

urlpatterns = [
    path('', include('departments.urls')),
    path('students/', include('students.urls')),
    path('users/', include('users.urls')),
]
