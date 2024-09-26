from django.db import models

# Create your models here.

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name

class Designation(models.Model):
    des_id = models.AutoField(primary_key=True)
    des_name = models.CharField(max_length=100)

    def __str__(self):
        return self.des_name

class EmployeeType(models.Model):
    empt_id = models.AutoField(primary_key=True)
    empt_name = models.CharField(max_length=50)

    def __str__(self):
        return self.empt_name

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    employee_type = models.ForeignKey(EmployeeType, on_delete=models.CASCADE)
    joined = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name
