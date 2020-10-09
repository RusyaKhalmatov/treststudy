from django.contrib.auth.models import User
from django.shortcuts import render
from django.template import RequestContext

from profileApp.models import Profile


def get_users_role_proc(request):
    print(request.user)
    if not request.user.is_anonymous:
        user = request.user
        user_profile = Profile.objects.get(user_id=user.id)
        context = {
            'user_role': user_profile.role.role_name
        }
    else:
        context = {}

    return context

#
# def view_base(request):
#     return render('../base.html',context=RequestContext(request,processors=[get_users_role_proc]))
