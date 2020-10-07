from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.base import View
from .forms import UserFormCreation, AddBookForm, ProfileForm
from profileApp.models import Student, Teachers, Profile



def index(request):
    return render(request, './index.html')


def student_list(request):
    print("Students list")
    student_list = []
    users = Profile.objects.all()
    for user in users:
        print(user.role)
        if (str(user.role) == 'student'):
            print(user.user.username)
            student_list.append(user)

    return render(request, 'students/students_list.html', {"students_list": student_list})


class StudentDetailView(View):

    def get(self, request, slug):
        student = get_object_or_404(Student, url=slug)
        return render(request, 'students/student_detail.html', {'student': student})


class TeachersList(View):
    def get(self, request):
        teachers = Teachers.objects.all()
        return render(request, 'teachers/teachers_list.html', {"teachers_list": teachers})


class TeacherDetailView(View):
    def get(self, request, slug):
        teacher = get_object_or_404(Teachers, url=slug)
        return render(request, 'teachers/teacher_detail.html', {"teacher": teacher})


#@login_required
#@transaction.atomic
def registerPage(request):
    print("Here again")
    if request.method == 'POST':
        print("Im in post part")
        # form = UserFormCreation(request.POST, instance=request.user)
        # extend_form = ProfileForm(request.POST, instance=request.user.profile)
        form = UserFormCreation(request.POST)
        extend_form = ProfileForm(request.POST)
        if form.is_valid() and extend_form.is_valid():
            user = form.save()
            profile = extend_form.save(commit=False)
            profile.user = user
            profile.url = 'url' + user.username
            profile.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            print("User successfully added ")
            return redirect('index')
    else:
        print("Im in else part")
        # form = UserFormCreation(instance=request.user)
        # extend_form = ProfileForm(instance=request.user.profile)
        form = UserFormCreation(request.POST)
        extend_form = ProfileForm(request.POST)
        context = {"form": form,
                   "extendform": extend_form}
    return render(request, 'accounts/register.html', context)


def addBook(request):
    print("Enter add book")
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date_published = timezone.now()
            post.save()
            return redirect('login')
    else:
        form = AddBookForm()
    return render(request, 'accounts/add_book.html', {'form': form})



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

