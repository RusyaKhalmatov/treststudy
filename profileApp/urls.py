from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('studentslist', views.student_list, name='profile_students_list'),
    path('student/<str:slug>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('teachers_list', views.TeachersList.as_view(), name="teachers_list"),
    path('teacher/<str:slug>/', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('register', views.registerPage, name="register"),
    path('login', views.loginPage, name="login"),
    path('add-book', views.addBook, name='addBook'),
    path('add-course', views.addCourse, name='add-course'),
    path('course-list', views.courseList, name='course-list'),
    path('course/<str:slug>/', views.courseDetail.as_view(), name='course-detail')

]
