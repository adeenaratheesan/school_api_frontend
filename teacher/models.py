from django.db import models

# Create your models here.
class Teacher(models.Model):
    name=models.CharField(max_length=100)
    age=models.BigIntegerField()
    gender=models.CharField(max_length=50)
    subject=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    class Meta:
        db_table='teacher_tb'
