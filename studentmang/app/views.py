from django.shortcuts import render,get_object_or_404
from app.models import Student
from app.forms import StudentForm
from django.contrib import messages


def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request,"Student details added successfully")
            form = StudentForm()
        else:
            messages.error(request,"Please check your details")

    else:
        form = StudentForm()



    return render(request,"add_std.html",{"form":form})

def get_all_std(request):

    get_data = Student.objects.all()

    return render(request,"std_list.html",{"get_data":get_data})

def get_single_std(request,id):

    student = get_object_or_404(Student,id=id)

    return render(request,"single_std.html",{"student":student})

def update_student(request,id):

    student = get_object_or_404(Student,id=id)

    if request.method == "POST":
        form = StudentForm(request.POST,request.FILES,instance=student)

        if form.is_valid():
            form.save()
            messages.success(request,"Student updated successfully")
        else:
            messages.error(request,"Please check your details")

    else:
        form = StudentForm(instance=student)

    return render(request,"update_std.html",{"student":student})