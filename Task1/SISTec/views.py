from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    s = "<h1> This is a SISTec Page </h1> <br> <h3>Sagar Institute of Science and Technology (SISTec) is a prominent technical and management institution group located in Bhopal, Madhya Pradesh, affiliated with RGPV and approved by AICTE. </h3> <br> <h2>Overview & Campuses </h2> <br> <p>SISTec Gandhi Nagar: The main campus located near the airport offering flagship engineering and management programs <br> SISTec-R (Ratibad): Located in Sikandrabad, Ratibad, focusing on multi-disciplinary research and engineering/management disciplines</p>"
    return HttpResponse(s)