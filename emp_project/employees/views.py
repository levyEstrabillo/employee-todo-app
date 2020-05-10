from django.shortcuts import render, redirect
from . import forms
from . import models
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='accounts:login')
def employee_form(request,id=0):
    if id == 0:
        if request.method == 'POST':
            form = forms.EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('employee:emp_list')
        else:
            form = forms.EmployeeForm()
        return render(request, 'employees/employee_form.html', {'form':form})  
    else:
        employees = models.EmployeeInfo.objects.get(id=id)
        if request.method == 'POST':
            form = forms.EmployeeForm(request.POST, instance=employees)
            if form.is_valid():
                form.save()
                return redirect('employee:emp_list')
        else:
            form = forms.EmployeeForm(instance=employees)
            return render(request, 'employees/employee_form.html', {'form':form})  

            

def employee_list(request):
    employees = models.EmployeeInfo.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees })



def employee_delete(request, id):
    if request.method == 'POST':
        employee = models.EmployeeInfo.objects.get(pk=id)
        employee.delete()
        return redirect('employee:emp_list')
