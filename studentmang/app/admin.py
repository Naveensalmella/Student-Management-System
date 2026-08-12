from django.contrib import admin

from app.models import Student

# Register your models here.


class Studentadmin(admin.ModelAdmin):
    list_display = ["id","name","age","email","phone","image",]

admin.site.register(Student,Studentadmin)