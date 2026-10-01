
from django.db import models


class product(models.Model):

    p_name = models.CharField(max_length=50)

    p_price = models.CharField()

    p_offer = models.CharField(max_length=40)

    def __str__(self):
        return self.p_name