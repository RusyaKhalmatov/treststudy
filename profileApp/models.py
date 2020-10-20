from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


def image_folder_students(instance, filename):
    return 'student_{0}/{1}'.format(instance.u_id, filename)


def image_folder_teachers(instance, filename):
    return 'teacher_{0}/{1}'.format(instance.u_id, filename)


class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField('Role name', max_length=20, blank=False, null=False)

    def __str__(self):
        return self.role_name

    class Meta:
        db_table = 'roles'
        verbose_name = "Role"
        verbose_name_plural = "Roles"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    thirdname = models.CharField('Thirdname', max_length=30, blank=True, null=True)
    date_of_birth = models.DateField('Date of birth', null=True)
    phone_number = models.CharField("Phone number", max_length=50, blank=True, null=True, default="+998")
    photo = models.ImageField('Upload photo', blank=True, null=True, upload_to='account_photo/')
    region = models.CharField('Region of a Country', max_length=30,
                              help_text="Enter user's region (Fergana, Tashkent viloyat, Samarkand)",
                              default='Tashkent')
    city = models.CharField('City', max_length=30, help_text="Enter user's city (Fergana, Tashkent, Samarkand)",
                            default="Tashkent")
    passport_series = models.CharField('Passport series', max_length=5, blank=False, null=False,
                                       help_text="two letters", default='aa')
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, blank=True, null=True)
    passport_number = models.CharField('Passport number', max_length=10, blank=False, null=False)
    home_address = models.CharField('Home address', max_length=70, null=False)
    rating = models.PositiveSmallIntegerField('Rating', default=0)
    reg_date = models.DateField("Date of registration", null=True)
    out_date = models.DateField("Out date ", null=True)
    url = models.SlugField(max_length=50, null=True, default="none")

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={"slug": self.url})


class Teacher(models.Model):
    u_id = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.u_id.user.username

    def get_absolute_url(self):
        return reverse('teacher_detail', kwargs={"slug": self.url})

    class Meta:
        db_table = 'teachers'
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"


class Dean(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.user.first_name

    class Meta:
        db_table = 'deans'
        verbose_name = "dean"
        verbose_name_plural = "deans"


class Faculty(models.Model):
    f_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=30, blank=False, null=False)
    dean = models.ForeignKey(Dean, on_delete=models.DO_NOTHING)
    url = models.SlugField(max_length=50, blank=True, null=True, default="none")

    def __str__(self):
        return self.f_name

    class Meta:
        db_table = 'faculties'


class Subject(models.Model):
    sub_id = models.AutoField(primary_key=True)
    sub_name = models.CharField('Subject name', max_length=20, blank=False, null=False)
    room_number = models.PositiveSmallIntegerField('Room number')
    teacher = models.ManyToManyField(Teacher)
    url = models.SlugField(max_length=50,blank=True, null=True, default="none")

    def __str__(self):
        return self.sub_name

    def get_absolute_url(self):
        return reverse('student-subject-detail', kwargs={"slug": self.url})

    class Meta:
        db_table = 'subjects'
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_level = models.PositiveSmallIntegerField('Course level', blank=False, null=False)
    course_name = models.CharField('Course name', max_length=150, blank=False, null=False)
    url = models.SlugField(max_length=50, blank=True, null=True,default="none")
    f_id = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.course_name

    class Meta:
        db_table = 'courses'
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    g_name = models.CharField('Group name', max_length=30, blank=False, null=False)
    date_start = models.DateField(null=False)
    date_end = models.DateField(null=True)
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    url = models.SlugField(max_length=50,blank=True, null=True, default="none")

    def __str__(self):
        return self.g_name

    class Meta:
        db_table = 'classes'
        verbose_name = "class"
        verbose_name_plural = "classes"


class Student(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    group = models.ForeignKey(Class, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={"slug": self.url})

    def __str__(self):
        return self.user.user.username

    class Meta:
        db_table = "students"
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField('Book name', max_length=50, blank=False, null=False)
    book_author = models.CharField('Book author', max_length=30, blank=False, null=False)
    date_published = models.DateField()
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.book_name

    class Meta:
        db_table = 'books'
        verbose_name = "Book"
        verbose_name_plural = "Books"
