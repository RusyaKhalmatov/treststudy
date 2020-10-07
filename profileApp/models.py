from django.db import models
from django.contrib.auth.models import User
# Create your models here#
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


def image_folder_students(instance, filename):
    return 'student_{0}/{1}'.format(instance.u_id, filename)


def image_folder_teachers(instance, filename):
    return 'teacher_{0}/{1}'.format(instance.u_id, filename)


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField('Book name', max_length=50, blank=False, null=False)
    book_author = models.CharField('Book author', max_length=30, blank=False, null=False)
    date_published = models.DateField()

    def __str__(self):
        return self.book_name

    class Meta:
        db_table = 'books'
        verbose_name = "Book"
        verbose_name_plural = "Books"


class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    dean = models.CharField(max_length=30, blank=False, null=False)
    course_name = models.CharField('Course name', max_length=150, blank=False, null=False)

    def __str__(self):
        return self.course_name

    class Meta:
        db_table = 'courses'
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Groups(models.Model):
    g_id = models.AutoField(primary_key=True)
    course_level = models.PositiveSmallIntegerField('Course level', blank=False, null=False)
    g_name = models.CharField('Group name', max_length=30, blank=False, null=False)
    date_start = models.DateField(null=False)
    date_end = models.DateField(null=True)
    course_id = models.ManyToManyField(Courses)

    def __str__(self):
        return self.g_name

    class Meta:
        db_table = 'groups'
        verbose_name = "Group"
        verbose_name_plural = "Groups"


class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField('Role name', max_length=20, blank=False, null=False)

    def __str__(self):
        return self.role_name

    class Meta:
        db_table = 'roles'
        verbose_name = "Role"
        verbose_name_plural = "Roles"


class Subjects(models.Model):
    sub_id = models.AutoField(primary_key=True)
    sub_name = models.CharField('Subject namem', max_length=20, blank=False, null=False)
    sub_book_id = models.ManyToManyField(Books)
    room_number = models.PositiveSmallIntegerField('Room number')

    def __str__(self):
        return self.sub_name

    class Meta:
        db_table = 'subjects'
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    thirdname = models.CharField('Thirdname', max_length=30, blank=True, null=True)
    date_of_birth = models.DateField('Date of birth', null=True)
    phone_number = models.CharField("Phone number", max_length=50, blank=True, null=True, default="+998")
    photo = models.ImageField('Upload photo', blank=True, null=True, upload_to='account_photo/')
    region = models.CharField('Region of a Country', max_length=30,
                              help_text="Enter user's region (Fergana, Tashkent viloyat, Samarkand)", default='Tashkent')
    city = models.CharField('City', max_length=30, help_text="Enter user's city (Fergana, Tashkent, Samarkand)")
    passport_series = models.CharField('Passport series', max_length=5, blank=False, null=False,
                                       help_text="two letters")
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, null=True)
    passport_number = models.CharField('Passport number', max_length=10, blank=False, null=False)
    home_address = models.CharField('Home address', max_length=70, null=False)
    rating = models.PositiveSmallIntegerField('Rating', default=0)
    reg_date = models.DateField("Date of registration", null=True)
    out_date = models.DateField("Out date ", null=True)
    url = models.SlugField(max_length=50,null=True, default="none")

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.user.username


class Student(models.Model):
    u_id = models.OneToOneField(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={"slug": self.url})

    def __str__(self):
        return self.u_id.username

    class Meta:
        db_table = "students"
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Teachers(models.Model):
    u_id = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subjects)

    def __str__(self):
        return self.u_id.username

    def get_absolute_url(self):
        return reverse('teacher_detail', kwargs={"slug": self.url})

    class Meta:
        db_table = 'teachers'
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
