from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    birth_day = models.DateField()


class Group(models.Model):
    name = models.CharField(max_length=10)
    curator = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)


class Student(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    course = models.IntegerField(default=1)
    enrollment_date = models.DateField()


class Lecturer(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)


class Discipline(models.Model):
    name = models.CharField(max_length=200)
    lecturer = models.ForeignKey(Lecturer, null=True, on_delete=models.SET_NULL)


class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    course = models.IntegerField()
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    grade = models.IntegerField()

