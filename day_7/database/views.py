from django.shortcuts import render
from django.http import HttpResponseRedirect
from database.models import Employee
from django.urls import reverse


# =========================
# CREATE
# =========================

def newEmployeeForm(request):
    return render(request, 'newEmployeeForm.html')


def saveuser(request):

    eno = request.POST['eno']
    ename = request.POST['ename']
    esal = request.POST['esal']

    emp = Employee(
        eno=eno,
        ename=ename,
        esal=esal
    )

    emp.save()

    url = reverse('Employeelist')
    return HttpResponseRedirect(url)


# =========================
# READ
# =========================

def Employeelist(request):

    Employees = Employee.objects.all()

    return render(
        request,
        'Employeelist.html',
        {'Employees': Employees}
    )


# =========================
# UPDATE FORM
# =========================

def updateEmployeeForm(request):

    id = request.GET.get('id')

    employee = Employee.objects.filter(id=id).values()

    return render(
        request,
        'updateEmployeeForm.html',
        {'employee': employee[0]}
    )


# =========================
# UPDATE
# =========================

def updateEmployee(request):

    id = request.POST['id']
    eno = request.POST['eno']
    ename = request.POST['ename']
    esal = request.POST['esal']

    Employee.objects.filter(id=id).update(
        eno=eno,
        ename=ename,
        esal=esal
    )

    url = reverse('Employeelist')
    return HttpResponseRedirect(url)


# =========================
# DELETE
# =========================

def deleteEmployee(request):

    id = request.GET.get('id')

    if id:
        Employee.objects.filter(id=id).delete()

    url = reverse('Employeelist')
    return HttpResponseRedirect(url)