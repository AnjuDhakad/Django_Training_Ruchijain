from django.shortcuts import render


def home(request):
    return render(request, 'main.html')


def sistec(request):
    return render(request, 'SISTec.html')


def lnct(request):
    return render(request, 'LNCT.html')


def oist(request):
    return render(request, 'OIST.html')
