from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='student-index'),
    path('subject/<str:slug>/', views.SubjectDetail.as_view(), name='student-subject-detail'),

]
