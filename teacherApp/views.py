from django.shortcuts import render


# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from profileApp.serializers import SubjectSerializer
from profileApp.templates.helper_functions.helper import get_teachers_subjects


def index(request):
    print('Student index')
    return render(request, './tea_index.html')


class TeacherSubjects(APIView):
    def get(self, request):
        teacher_subjects_list = get_teachers_subjects(request.user)
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = SubjectSerializer(teacher_subjects_list, many=True)
        return Response({"Subjects": serializer.data})