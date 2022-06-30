from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
from simple_history.models import HistoricalRecords


class Question(models.Model):

    name = models.CharField(max_length=200, null=True)

    class Answer(models.IntegerChoices):
        a = 1
        b = 2
        c = 3
        d = 4
        e = 5
        f = 6

    val = models.IntegerField(choices=Answer.choices, blank=True, null=True)

    def __str__(self):
        return self.name

class Quiz(models.Model):

    name = models.CharField(max_length=200, null=True, default='360')
    uname = models.ForeignKey(User, null=True, related_name='ownership', on_delete=models.SET_NULL)
    res = models.CharField(max_length=200, null=True)
    questions = models.ManyToManyField(Question)
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.name

# class Project(models.Model):

#     name = models.CharField(max_length=200, null=True)
#     description = models.CharField(max_length=2000, null=True, blank=True)
#     status = models.CharField(max_length=200, null=True)
#     date_created= models.DateTimeField(auto_now_add=True, null=True)

#     owner = models.ForeignKey(Student, null=True, related_name='ownership', on_delete=models.SET_NULL)
#     participants = models.ManyToManyField(Student)

#     def __str__(self):
#         return self.name

# class Event(models.Model):

#     name = models.CharField(max_length=200, null=True)
#     description = models.CharField(max_length=2000, null=True, blank=True)
#     ev_date = models.DateTimeField(null=True)
#     place = models.CharField(max_length=200, null=True)
#     date_created= models.DateTimeField(auto_now_add=True, null=True)

#     participants = models.ManyToManyField(Student)

#     def __str__(self):
#         return self.name