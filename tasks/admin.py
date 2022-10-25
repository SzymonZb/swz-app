from django.contrib import admin
from .models import Task, Employee, TaskTag, TaskUpdate

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status']
    list_filter = ['title', 'status']


# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ['employee', 'name', 'phone', 'email', 'date_created']
#     list_filter = ['name', 'phone', 'email', 'date_created']

admin.site.register(TaskTag)
admin.site.register(Employee)
admin.site.register(TaskUpdate)

