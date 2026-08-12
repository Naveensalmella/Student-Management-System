from django.shortcuts import render,get_object_or_404,redirect
from app.models import Student
from app.forms import StudentForm
from django.contrib import messages


def home(request):

    total_students = Student.objects.count()

    return render(request,"home.html",{"total_students":total_students})


def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request,"Student details added successfully")
            return redirect("get_all_std")
        else:
            messages.error(request,"Please check your details")

    else:
        form = StudentForm()

    return render(request,"add_std.html",{"form":form})


def get_all_std(request):

    query = request.GET.get("q","")

    if query:
        get_data = Student.objects.filter(name__icontains=query)
    else:
        get_data = Student.objects.all()

    return render(request,"std_list.html",{"get_data":get_data,"query":query})


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
            return redirect("get_single_std",id=student.id)
        else:
            messages.error(request,"Please check your details")

    else:
        form = StudentForm(instance=student)

    return render(request,"update_std.html",{"student":student,"form":form})


def delete_student(request,id):

    student = get_object_or_404(Student,id=id)

    if request.method == "POST":
        student.delete()
        messages.success(request,"Student deleted successfully")
        return redirect("get_all_std")

    return render(request,"confirm_delete.html",{"student":student})
