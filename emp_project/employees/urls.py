from django.urls import path
from . import views

app_name='employee'

urlpatterns = [
    path('', views.employee_form, name='emp_form'),
    path('<id>', views.employee_form, name='emp_form'),
    path('list/', views.employee_list, name='emp_list'),
    path('delete/<id>', views.employee_delete, name='emp_delete'),
]