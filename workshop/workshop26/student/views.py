from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm 
# Create your views here.


def list(request):
    students = Student.objects.all()
    return render(request,"student/list.html",{"students":students})
    
def create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            age = form.cleaned_data.get("age")
        
            Student.objects.create(name=name,age=age)
            
            return redirect("student:list")

    else:
        return render(request,"student/create.html")
    

    
    


