from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myinfo(request):
    s="<h1>Anju Dhakad</h1> <br> <h1>0187AS241025<h1/>"

    return HttpResponse(s)

def collage(request):
    s="<h1>Sagar Intitute of Science and Technology Gandhi nagar bhopal</h1>"
    return HttpResponse(s)

def department(request):
    s="<h1>Artificial intelligence and data science</h1>"
    return HttpResponse(s)
