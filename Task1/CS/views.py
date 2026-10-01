from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def aboutCs(request):
    s = "<h1> This is a CS Page </h1> <br> <p>The Department of Computer Science & Engineering (CSE) at SISTec Bhopal offers a 4-year undergraduate B.Tech program focused on software development, core programming, and modern technologies</p>"
    return HttpResponse(s)