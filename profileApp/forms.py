from datetime import datetime

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from profileApp.models import Books, Profile, Courses


class UserFormCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('thirdname', 'phone_number', 'passport_number','passport_series', 'date_of_birth','home_address','role')


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('book_name', 'book_author')


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ('dean', 'course_name')


class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('thirdname', 'phone_number', 'passport_number')




