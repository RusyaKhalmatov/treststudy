from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from .views import TeachersList, StudentDetailView, TeacherDetailView, courseDetail

urlpatterns = [
    path('', views.index, name='index'),
    path('studentslist', views.student_list, name='profile_students_list'),
    path('student/<str:slug>/', login_required(StudentDetailView.as_view(), login_url='login'), name='student_detail'),
    path('teachers_list', login_required(TeachersList.as_view(), login_url='login'), name="teachers_list"),
    path('teacher/<str:slug>/', login_required(TeacherDetailView.as_view(), login_url='login'), name='teacher_detail'),
    path('register', views.registerPage, name="register"),
    path('register-student', views.registerStudentPage, name="register-student"),
    # path('register-teacher', views.registerTeacherPage, name="register-teacher"),
    path('login', views.loginPage, name="login"),
    path('logout/', views.logoutView, name='logout'),
    path('add-book', views.addBook, name='addBook'),
    path('add-course', views.addCourse, name='add-course'),
    path('add-subject', views.addSubject, name='add-subject'),
    path('course-list', views.courseList, name='course-list'),
    path('course/<str:slug>/', login_required(courseDetail.as_view(), login_url='login'), name='course-detail'),
    path('user',views.userPage, name='userPage')


]
