from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic.base import View

from profileApp.models import Subject


def index(request):
    print('Student index')
    return render(request, './st_index.html')


def side(request):
    return render(request, 'left-sidebar/left_sidebar.html')


class SubjectDetail(View):
    def get(self, request, slug):
        subject = get_object_or_404(Subject, url=slug)
        return render(request, 'subject/subject_base.html', {'subject': subject})
