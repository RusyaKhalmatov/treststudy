from datetime import datetime

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from profileApp.models import Books, Profile


class UserFormCreation(UserCreationForm):
    # email = forms.EmailField(required=True)
    # firstname = forms.CharField(max_length=50, required=True)
    # username = forms.CharField(max_length=50, required=True)
    # lastname = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        # print("save form")
        # user.email = self.cleaned_data['email']
        # user.first_name = self.cleaned_data['first_name']
        # user.last_name = self.cleaned_data['last_name']
        # user.username = self.cleaned_data['username']
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


class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('thirdname', 'phone_number', 'passport_number')



