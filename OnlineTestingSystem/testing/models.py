
from django.db import models
from django.contrib.auth.models import User
class TestResult(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    test_name = models.CharField(max_length=100)

    total_questions = models.IntegerField()

    attempted = models.IntegerField()

    correct = models.IntegerField()

    wrong = models.IntegerField()

    skipped = models.IntegerField()

    score = models.IntegerField()

    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.test_name}"
# Create your models here.
