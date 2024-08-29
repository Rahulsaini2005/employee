from django.db import models

from employee.custom import DateTimeModel


class Employee(DateTimeModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True, max_length=30)
    dob = models.DateField(null=True)
    department = models.CharField(max_length=50)

