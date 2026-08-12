from django import forms
from app.models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ["name","age","email","course","phone","image"]
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter student name"}),
            "age": forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter age"}),
            "email": forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter email"}),
            "course": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter course"}),
            "phone": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter phone number"}),
            "image": forms.ClearableFileInput(attrs={"class":"form-control"}),
        }
