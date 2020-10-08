from django.http import HttpResponse
from django.shortcuts import redirect


# не показывать страницу логирования если пользователь залогинился в систему
def authenticate_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


# рахрешение просмотра страницы по ролям
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Вы не авторизованы чтобы просматривать эту страницу')

        return wrapper_func

    return decorator


# разрешение просматривать страницу только администратору
def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('user-page')
