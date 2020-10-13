from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic.base import View

from .decorators import authenticate_required, allowed_users
from .forms import UserFormCreation, AddBookForm, ProfileForm, AddCourseForm, AddSubjectForm, AddTeacherForm, \
    AddStudentForm
from profileApp.models import Student, Teacher, Profile, Course, Roles, Dean
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# @allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def index(request):
    return render(request, './index.html')


@login_required(login_url='login')
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
        teacher_list = []
        teachers = Profile.objects.all()
        for t in teachers:
            if str(t.role) == 'teacher':
                teacher_list.append(t)
        return render(request, 'teachers/teachers_list.html', {"teachers": teacher_list})

class TeacherDetailView(View):
    def get(self, request, slug):
        user = get_object_or_404(Profile, url=slug)
        return render(request, 'teachers/teacher_detail.html', {"user": user})


# start register page
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def registerPage(request):
    if request.method == 'POST':
        form = UserFormCreation(request.POST)
        extend_form = ProfileForm(request.POST)
        if form.is_valid() and extend_form.is_valid():
            user = form.save()
            profile = extend_form.save(commit=False)
            profile.user = user
            profile.url = 'url' + user.username
            user_role = extend_form.cleaned_data['role']
            group = Group.objects.get(name=user_role)
            profile.role=user_role
            profile.save()
            user.groups.add(group)
            if str(user_role) == 'admin':
                user.is_staff = True
            elif str(user_role) == 'dean':
                user.is_staff = True
                dean = Dean.objects.create(user=profile)

            user.save()

            return redirect('index')
    else:
        form = UserFormCreation(request.POST)
        extend_form = ProfileForm(request.POST)

    context = {"form": form,
               "extendform": extend_form}
    return render(request, 'accounts/register.html', context)


@login_required(login_url='login')
def addBook(request):
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date_published = timezone.now()
            post.save()
            book_name = form.cleaned_data['book_name']
            messages.success(request, "Книга " + book_name + " успешно добавлена")
    else:
        form = AddBookForm()
    return render(request, 'add_book.html', {'form': form})


@login_required(login_url='login')
def addCourse(request):
    alert = False
    if request.method == "POST":
        form = AddCourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.url = 'course-' + str(course.course_id)
            course.save()
            alert = True
    else:
        form = AddCourseForm()
    return render(request, 'courses/add-course.html', {'form': form, 'alert': alert})


class courseDetail(View):
    def get(self, request, slug):
        course = get_object_or_404(Course, url=slug)
        return render(request, 'courses/course_detail.html', {"course": course})


@login_required(login_url='login')
def courseList(request):
    course = Course.objects.all()
    print(course)
    return render(request, 'courses/course_list.html', {"courses": course})


@authenticate_required
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Неправильный логин или пароль")

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutView(request):
    logout(request)
    return redirect('login')


def userPage(request):
    context = {}
    return render(request, 'accounts/user', context)


@login_required(login_url='login')
def registerStudentPage(request):
    if request.method == 'POST':
        form = UserFormCreation(request.POST)
        extend_form = ProfileForm(request.POST)
        s_form = AddStudentForm(request.POST)
        if form.is_valid() and extend_form.is_valid() and s_form.is_valid():
            role_student = Roles.objects.get(role_name='student')
            print("ROLE-ROLE-ROLE -- " + str(role_student.role_name))
            user = form.save()
            profile = extend_form.save(commit=False)
            student = s_form.save(commit=False)
            profile.user = user
            profile.url = 'url' + user.username
            profile.role = role_student
            group = Group.objects.get(name=role_student.role_name)
            student.save()
            profile.save()
            student.user = profile
            user.groups.add(group)
            user.save()
            return redirect('index')
    else:
        form = UserFormCreation(request.POST)
        extend_form = ProfileForm(request.POST)
        s_form = AddStudentForm(request.POST)
    context = {"form": form,
               "extendform": extend_form,
               "s_form": s_form
               }
    return render(request, 'accounts/register-student.html', context)

@login_required(login_url='login')
def addSubject(request):
    if request.method == "POST":
        form = AddSubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.url = str(subject.sub_name) + str(subject.room_number) + 'url'
            subject.save()
            messages.success(request, "Предмет " + subject.sub_name + " успешно добавлена")
    else:
        form = AddSubjectForm()
    return render(request, 'add_subject.html', {'form': form})


