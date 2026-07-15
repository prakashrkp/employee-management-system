from django.shortcuts import render,redirect
from .models import Employee
from .form import EmployeeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def employee_list(request):

    search = request.GET.get('search')

    if search:
        employees = Employee.objects.filter(
            name__icontains=search
        )
    else:
        employees = Employee.objects.all()


    return render(request,'employee_list.html',{
        'employees':employees
    })


def add_employee(request):

    if request.method == 'POST':

        form = EmployeeForm(request.POST)

        if form.is_valid():

            emp = form.save()

            messages.success(
                request,
                f"Employee '{emp.name}' added successfully by {request.user.username}!"
            )

            return redirect('/employees/')

    else:

        form = EmployeeForm()

    return render(request, 'add_employee.html', {
        'form': form
    })
@login_required
def update_employee(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == "POST":

        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.phone = request.POST['phone']
        employee.department = request.POST['department']
        employee.salary = request.POST['salary']

        employee.save()

        return redirect('/employees/')

    return render(request, 'update_employee.html', {
        'employee': employee
    })
@login_required
def delete_employee(request, id):

    employee = Employee.objects.get(id=id)

    employee.delete()

    return redirect('/employees/')

def user_login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(request, user)

            return redirect('/dashboard/')


    return render(request, 'login.html')

def user_logout(request):

    logout(request)

    return redirect('/login/')