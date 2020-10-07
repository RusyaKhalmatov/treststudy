from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('studentslist', views.student_list, name='profile_students_list'),
    path('student/<slug:slug>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('teachers_list', views.TeachersList.as_view(), name="teachers_list"),
    path('teacher/<slug:slug>/', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('register', views.registerPage, name="register"),
    path('login', views.loginPage, name="login"),
    path('add-book', views.addBook, name='addBook')
]
