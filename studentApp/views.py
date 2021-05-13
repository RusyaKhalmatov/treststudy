from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic.base import View
from rest_framework.response import Response
from rest_framework.views import APIView

from profileApp.models import Subject
from profileApp.templates.helper_functions.helper import get_course_subject_by_student
from profileApp.serializers import SubjectSerializer


def index(request):
    print('Student index')
    return render(request, './st_index.html')


def side(request):
    return render(request, 'left-sidebar/left_sidebar.html')


class SubjectDetail(View):
    def get(self, request, slug):
        subject = get_object_or_404(Subject, url=slug)
        return render(request, 'subject/subject_base.html', {'subject': subject})


class SubjectsListView(APIView):
    def get(self, request):
        student_subjects_list = get_course_subject_by_student(request.user)
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = SubjectSerializer(student_subjects_list, many=True)
        return Response({"Subjects": serializer.data})
