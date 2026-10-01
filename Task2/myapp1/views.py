from django.shortcuts import render

def testpaper(request):
    return render(request, 'testpaper.html')