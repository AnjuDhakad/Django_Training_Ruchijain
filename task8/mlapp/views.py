from django.shortcuts import render, redirect
from django.conf import settings
from .models import Student
import joblib
import os


def home(request):
    return render(request, 'home.html')


def studentregister(request):
    return render(request, 'studentregister.html')


def save_student(request):

    if request.method == 'POST':

        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        password = request.POST.get('password')
        branch = request.POST.get('branch')
        student_number = request.POST.get('student_number')
        email = request.POST.get('email')

        Student.objects.create(
            student_id=student_id,
            name=name,
            password=password,
            branch=branch,
            student_number=student_number,
            email=email
        )

        return redirect('login')

    return redirect('studentregister')


def login(request):
    return render(request, 'login.html')


def login_validation(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        password = request.POST.get('password')

        student = Student.objects.filter(
            name=name,
            password=password
        ).first()

        if student:

            return render(
                request,
                'studentprediction.html',
                {
                    'student': student
                }
            )

        else:

            return render(
                request,
                'login.html',
                {
                    'error': 'Invalid student name or password'
                }
            )

    return redirect('login')


def studentprediction(request):
    return render(request, 'studentprediction.html')


def result(request):

    if request.method == 'POST':

        # ML model file path
        model_path = os.path.join(
            settings.BASE_DIR,
            'mlmodel (1).pkl'
        )

        # Scaler file path
        scaler_path = os.path.join(
            settings.BASE_DIR,
            'scalermodel (1).pkl'
        )

        # Load model and scaler
        mlmodel = joblib.load(model_path)
        scaler = joblib.load(scaler_path)

        # Get input values
        iq = float(request.POST.get('iq'))
        cgpa = float(request.POST.get('cgpa'))
        profile_score = float(
            request.POST.get('profile_score')
        )

        # Input data
        data = [
            iq,
            cgpa,
            profile_score
        ]

        # Scale input
        scaled_input = scaler.transform([data])

        # Prediction
        ans = mlmodel.predict(scaled_input)[0]

        # Convert prediction into integer
        ans = int(ans)

        # Result message
        if ans == 1:

            message = "Congratulations! You're Placed 🎉"

        else:

            message = (
                "You need to study more "
                "and improve your skills."
            )

        return render(
            request,
            'result.html',
            {
                'ans': ans,
                'message': message,
                'data': data
            }
        )

    return redirect('studentprediction')