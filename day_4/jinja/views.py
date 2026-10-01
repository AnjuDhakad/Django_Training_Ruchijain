from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def testpaper(request):
    que="Who developed python?"
    a="dennis ritchide"
    b="Guide ven rossum"
    c="Anju Dhakad"
    d="Alisha khan" 
    context={
        'que':que,
        'a':a,
        'b':b,
        'c':c,
        'd':d,
    }
    template=loader.get_template('testpaper.html')
    res=template.render(context,request)
    return HttpResponse(res)

def info(request):
    name="Anju Dhakad"
    Dep="AIDS"
    Age="20"
    context={
        'name':name,
        'Dep':Dep,
        'Age':Age
    }
    template=loader.get_template('info.html')
    res=template.render(context,request)
    return HttpResponse(res)

def sum(request):
    a=12
    b=20
    c=30
    result=a+b+c
    context = {
        'a': a,
        'b': b,
        'c': c,
        'result':result
    }
   
    template=loader.get_template('add.html')
    res=template.render(context,request)
    return HttpResponse(res)

def result(request):
    context={
        'name':"Anju Dhakad",
        'marks':82

    }
    return render(request,'result.html',context)
def boting(request):
    context={
        'name':"Anju Dhakad",
        'age':20,
        'country':"India"
    }
    return render(request,'boting.html',context)

 

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')