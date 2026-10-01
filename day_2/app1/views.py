from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    s = "<h1>This is home page</h1>"
    return HttpResponse(s)
def about(request):
    s = "<h1>This is about page</h1>"
    return HttpResponse(s)
