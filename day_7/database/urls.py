from django.urls import path
from . views import *

urlpatterns = [
    
    path('deleteEmployee/',deleteEmployee,name='deleteEmployee'),
    path('updateEmployee/',updateEmployee,name='updateEmployee'),
    path('saveuser/',saveuser,name='saveuser'),
    path('Employeelist/',Employeelist,name='Employeelist'),
    path('newEmployeeForm/',newEmployeeForm,name='newEmployeeForm'),
    path('updateEmployeeForm/',updateEmployeeForm,name='updateEmployeeForm'),
]
