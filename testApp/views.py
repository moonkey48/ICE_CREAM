from django.shortcuts import render, redirect
from .models import AiClass, AiStudent


# Create your views here.


def home(request):
    class_object = AiClass.objects.all()
    student_object = AiStudent.objects.all()
    return render(request, 'test/home.html', {'class_object': class_object, 'student_object': student_object})


def result(request):
    name = request.POST['username']
    students = ['inu', 'james', 'bob']

    if name in students:
        is_exist = True
    else:
        is_exist = False

    return render(request, 'test/result.html', {'user_name': name, 'is_exist': is_exist})


def add(request):
    if request.method == 'POST':
        AiStudent.objects.create(
            name=request.POST['name']
        )
        return redirect('home')
    return render(request, 'test/add.html')
