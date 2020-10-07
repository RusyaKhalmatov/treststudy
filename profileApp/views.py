from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.base import View
from .forms import UserFormCreation, AddBookForm, ProfileForm, AddCourseForm
from profileApp.models import Student, Teachers, Profile, Courses


def index(request):
    return render(request, './index.html')


def student_list(request):
    student_list = []
    users = Profile.objects.all()
    for user in users:
        if str(user.role) == 'student':
            student_list.append(user)

    return render(request, 'students/students_list.html', {"students_list": student_list})


class StudentDetailView(View):
    def get(self, request, slug):
        student = get_object_or_404(Profile, url=slug)
        return render(request, 'students/student_detail.html', {'student': student})


class TeachersList(View):
    def get(self, request):
        teachers_list = []
        teachers = Profile.objects.all()
        for t in teachers:
            if str(t.role) == 'teacher':
                teachers_list.append(t)
        return render(request, 'teachers/teachers_list.html', {"teachers": teachers_list})


class TeacherDetailView(View):
    def get(self, request, slug):
        user = get_object_or_404(Profile, url=slug)
        return render(request, 'teachers/teacher_detail.html', {"user": user})


# @login_required
# @transaction.atomic
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
            # messages.success(request, _('Your profile was successfully updated!'))
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
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date_published = timezone.now()
            post.save()
            return redirect('login')
    else:
        form = AddBookForm()
    return render(request, 'add_book.html', {'form': form})


def addCourse(request):
    alert = False
    if request.method == "POST":
        form = AddCourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            course.url = 'course-' + str(course.course_id)
            course.save()
            alert = True
    else:
        form = AddCourseForm()
    return render(request, 'courses/add-course.html', {'form': form, 'alert': alert})


class courseDetail(View):
    def get(self, request, slug):
        course = get_object_or_404(Courses, url=slug)
        return render(request, 'courses/course_detail.html', {"course": course})


def courseList(request):
    courses = Courses.objects.all()
    return render(request, 'courses/course_list.html', {"courses": courses})


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
