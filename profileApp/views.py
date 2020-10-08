from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic.base import View
from .forms import UserFormCreation, AddBookForm, ProfileForm, AddCourseForm
from profileApp.models import Student, Teachers, Profile, Courses
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


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
@login_required(login_url='login')
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


@login_required(login_url='login')
def courseList(request):
    courses = Courses.objects.all()
    return render(request, 'courses/course_list.html', {"courses": courses})


def loginPage(request):
    if request.user.is_authenticated:
        print("I A AUTHENTICATED")
        return redirect('index')
    else:
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
