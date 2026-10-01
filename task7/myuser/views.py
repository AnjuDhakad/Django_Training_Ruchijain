from django.shortcuts import render, redirect
from .models import User, Student


# HOME PAGE
def home(request):
    return render(request, 'home.html')


# SIGNUP PAGE
def signup(request):
    return render(request, 'signup.html')


# SAVE USER
def saveuser(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if username already exists
        if User.objects.filter(username=username).exists():

            return render(
                request,
                'signup.html',
                {
                    'error': 'Username already exists!'
                }
            )

        User.objects.create(
            username=username,
            password=password
        )

        return redirect('login')

    return redirect('signup')


# LOGIN PAGE
def login(request):
    return render(request, 'login.html')


# LOGIN VALIDATION
def loginvalidation(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(
            username=username,
            password=password
        ).first()

        if user:

            request.session['username'] = user.username

            return redirect('studentform')

        else:

            return render(
                request,
                'login.html',
                {
                    'error': 'Invalid username or password!'
                }
            )

    return redirect('login')


# STUDENT FORM
def studentform(request):

    if 'username' not in request.session:
        return redirect('login')

    return render(
        request,
        'studentform.html',
        {
            'username': request.session['username']
        }
    )


# SAVE STUDENT
def savestudent(request):

    if 'username' not in request.session:
        return redirect('login')

    if request.method == 'POST':

        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        branch = request.POST.get('branch')

        Student.objects.create(
            name=name,
            number=number,
            email=email,
            branch=branch
        )

        return redirect('recordsaved')

    return redirect('studentform')


# RECORD SAVED
def recordsaved(request):

    if 'username' not in request.session:
        return redirect('login')

    return render(
        request,
        'recordsaved.html'
    )


# LOGOUT
def logout(request):

    request.session.flush()

    return redirect('home')