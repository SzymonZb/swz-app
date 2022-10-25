from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class TaskTag(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    TASK_STATUS = (
        ('UNASSIGNED', 'UNASSIGNED'),
        ('WORK_IN_PROGRESS', 'WORK_IN_PROGRESS'),
        ('DONE', 'DONE'),
        ('STOPPED', 'STOPPED')
    )
    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(choices=TASK_STATUS, default='UNASSIGNED', max_length=50)
    tags = models.ManyToManyField(TaskTag)

    def __str__(self):
        return self.title


class TaskUpdate(models.Model):
    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    task = models.ForeignKey(Task, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updates = models.CharField(max_length=1000, null=True)
