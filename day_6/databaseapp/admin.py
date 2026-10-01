from django.contrib import admin
from databaseapp.models import client
from databaseapp.models import customer
from databaseapp.models import order
admin.site.register(client)
admin.site.register(customer)
admin.site.register(order)
# Register your models here.

