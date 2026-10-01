from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path(
        'studentregister/',
        views.studentregister,
        name='studentregister'
    ),

    path(
        'save-student/',
        views.save_student,
        name='save_student'
    ),

    path(
        'login/',
        views.login,
        name='login'
    ),

    path(
        'login-validation/',
        views.login_validation,
        name='login_validation'
    ),

    path(
        'studentprediction/',
        views.studentprediction,
        name='studentprediction'
    ),

    path(
        'result/',
        views.result,
        name='result'
    ),
]