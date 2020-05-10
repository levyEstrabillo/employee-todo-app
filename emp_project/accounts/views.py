from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def account_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('employee:emp_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/account_login.html', {'form':form})

def account_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('employee:emp_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/account_signup.html', {'form':form})


def account_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')