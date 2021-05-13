from profileApp.models import Profile, Student, Class, Course, Teacher, Subject


def get_students():
    profiles = Profile.objects.all()
    students_list = []
    for profile in profiles:
        if str(profile.role.role_name) == 'student':
            students_list.append(profile)

    return students_list


def get_course_subject_by_student(user):
    profile_user = Profile.objects.get(user=user)
    student = Student.objects.get(user=profile_user)
    student_class = Class.objects.get(class_id=student.group.class_id)
    course = Course.objects.get(course_id=student_class.course_id.course_id)
    student_subjects = course.subject.all()
    return student_subjects


def get_student_class(user):
    profile_user = Profile.objects.get(user=user)
    student = Student.objects.get(user=profile_user)
    return student.group.g_name


def get_user_name(user):
    profile_user = Profile.objects.get(user=user)
    context = {
        'name': user.first_name,
        'last_name': user.last_name,
        'third_name': profile_user.thirdname,
    }
    return context


def get_teachers_subjects(user):
    profile_user = Profile.objects.get(user=user)
    teacher = Teacher.objects.get(u_id=profile_user)
    subjects = Subject.objects.filter(teacher=teacher)
    return subjects
