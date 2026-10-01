from django.db import models
class Student(models.Model):
    student_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    student_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.name