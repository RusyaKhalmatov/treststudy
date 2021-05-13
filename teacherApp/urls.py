from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='teacher-index'),
    path('subjects/', views.TeacherSubjects.as_view(), name='teacher-subjects-list'),


]
