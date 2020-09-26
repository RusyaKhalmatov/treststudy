from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from profileApp.models import Student, Teachers, UserExtend



def index(request):
    return HttpResponse("Hello, world. You're at the profile App index.")


def student_list(request):
    student_list=[]
    users = UserExtend.objects.all()
    for user in users:
        if (str(user.role )== "Student"):
            student_list.append(user)

    return render(request, 'students/students_list.html', {"students_list": student_list})


class StudentDetailView(View):

    def get(self, request, slug):
        student = get_object_or_404(Student, url = slug)
        return render(request,'students/student_detail.html', {'student':student})


class TeachersList(View):
    def get(self,request):
        teachers = Teachers.objects.all()
        return render(request, 'teachers/teachers_list.html', {"teachers_list":teachers})


class TeacherDetailView(View):
    def get(self, request, slug):
        teacher = get_object_or_404(Teachers, url=slug)
        return render(request, 'teachers/teacher_detail.html', {"teacher": teacher})



def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()


    context = {"form": form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)


#
# class StudentsView(ListView):
#     model = Student
#     queryset = Student.objects.all()
#     template_name = "students/students_list.html"
#
#
# class StudentDetailView(DetailView):  #Django будет искать template файл соответственно student_detail, что берется из названия
#     model = Student
#     slug_field = "url" #по столбцу url в таблице будет идти поиск

