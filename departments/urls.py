from django.urls import path

from . import views

app_name = 'departments'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
]
