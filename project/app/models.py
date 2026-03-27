from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10,null=True)
    age = models.IntegerField(null=True)
    course = models.CharField(max_length=10,primary_key=True)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return f'{self.name}-{self.age}-{self.course}-{self.date}'
class Course(models.Model):
    course = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='coursename')
    facultuname=models.CharField(max_length=10)
    def __str__(self):
        return f'{self.course}-{self.facultuname}'