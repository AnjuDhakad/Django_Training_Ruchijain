from django.db import models
from django.db import models

class client(models.Model):
    client_id=models.IntegerField()
    client_name=models.CharField(max_length=40)
    client_company=models.CharField(max_length=30)

    def __str__(self):
        return self.client_name



class customer(models.Model):
    customer_id=models.IntegerField()
    customer_name=models.CharField(max_length=40)
    customer_no=models.IntegerField()

    
    def __str__(self):
        return self.customer_name





class order(models.Model):
    order_id=models.IntegerField()
    order_name=models.CharField(max_length=40)
    order_price=models.FloatField()

    
    def __str__(self):
        return self.order_name

    
