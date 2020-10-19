from django.contrib.auth.models import User
from django.shortcuts import render
from django.template import RequestContext

from profileApp.models import Profile
from profileApp.templates.helper_functions.helper import get_course_subject_by_student


def get_users_role_proc(request):
    if not request.user.is_anonymous:
        user = request.user
        user_profile = Profile.objects.get(user_id=user.id)
        if str(user_profile.role.role_name) == 'student':
            student_subject_list = get_course_subject_by_student(user)  # get the list of a student's subject
            context = {
                'user_role': user_profile.role.role_name,
                'subject_list': student_subject_list
            }
        else:
            context = {
                'user_role': user_profile.role.role_name
            }
    else:
        context = {}

    return context


# def get_students_subjects(request):
#     if not request.user.is_anonymous:
#         user = request.user
#         user_profile = Profile.objects.get(user_id=user.id)
#         if str(user_profile.role.role_name) == 'student':
#             students
#
#         subjects_context = {
#             'user_role': user_profile.role.role_name
#         }
#     else:
#         context = {}
#
#     return subjects_context
#
# def view_base(request):
#     return render('../base.html',context=RequestContext(request,processors=[get_users_role_proc]))
