from django.db import models
from django.conf import settings

class Grade(models.Model):
    name = models.CharField(max_length=250)
    teachers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return f'{self.name}'

class Class(models.Model):
    name = models.CharField(max_length=250)
    teachers = models.ManyToManyField(settings.AUTH_USER_MODEL)
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE)

    def __str__(self):
        grade_in_str = f'{self.grade.name}'
        return f'{self.name}' + " Grado: " + grade_in_str

class Unit(models.Model):
    name = models.CharField(max_length=250, default="")
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE)
    clase = models.ForeignKey('Class', on_delete=models.CASCADE)

    def __str__(self):
        grade_in_str = f'{self.grade.name}'
        clase_in_str = f'{self.clase.name}'
        return f'{self.name}' + " Grado: " + grade_in_str + " Clase: " + clase_in_str

class Student(models.Model):
    name = models.CharField(max_length=250)
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE)
    classes = models.ManyToManyField('Class')

    def __str__(self):
        grade_in_str = f'{self.grade.name}'
        return f'{self.name}' + " Grado: " + grade_in_str

class Score(models.Model):
    name = models.CharField(max_length=250, default= "")
    description = models.CharField(max_length=250, default="")
    score = models.IntegerField()
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    clase = models.ForeignKey('Class', on_delete=models.CASCADE)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)

    def __str__(self):
        student_in_str = f'{self.student.name}'
        clase_in_str = f'{self.clase.name}'
        unit_in_str = f'{self.unit.name}'
        return f'{self.name}' + " Estudiante: " + student_in_str + " Clase: " + clase_in_str + " Unidad: " + unit_in_str 