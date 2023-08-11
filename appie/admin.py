from django.contrib import admin

from appie.models import Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','roll','city']


