from django.urls import path
from . import views


urlpatterns = [

    path(
        'home/',
        views.home,
        name='home'
    ),

    path(
        'signup/',
        views.signup,
        name='signup'
    ),

    path(
        'saveuser/',
        views.saveuser,
        name='saveuser'
    ),

    path(
        'login/',
        views.login,
        name='login'
    ),

    path(
        'loginvalidation/',
        views.loginvalidation,
        name='loginvalidation'
    ),

    path(
        'studentform/',
        views.studentform,
        name='studentform'
    ),

    path(
        'savestudent/',
        views.savestudent,
        name='savestudent'
    ),

    path(
        'recordsaved/',
        views.recordsaved,
        name='recordsaved'
    ),

    path(
        'logout/',
        views.logout,
        name='logout'
    ),
]