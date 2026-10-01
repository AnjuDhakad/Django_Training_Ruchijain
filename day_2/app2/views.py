from django.shortcuts import render
from django.http import HttpResponse

def linkedin(request):
    s = "<h1>This is linkedin page</h1>"
    return HttpResponse(s)
def facebook(request):
    s = "<h1>This is facebook page</h1>"
    return HttpResponse(s)

# Create your views here.
