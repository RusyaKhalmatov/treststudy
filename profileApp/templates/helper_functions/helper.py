from profileApp.models import Profile, Student, Class, Course


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


