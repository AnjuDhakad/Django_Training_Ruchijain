from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def aboutAids(request):
    s = "This is an AIDS Page <br> <p>The Sagar Institute of Science and Technology (SISTec) in Bhopal, " \
    "Madhya Pradesh, offers a dedicated B.Tech. in Computer Science and Engineering " \
    "(Artificial Intelligence and Data Science - AIDS) program</p>"
    return HttpResponse(s)