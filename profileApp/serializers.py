from abc import ABC

from rest_framework import serializers

from profileApp.models import Subject, Course, Teacher


# class SubjectSerializer(serializers.Serializer):
class SubjectSerializer(serializers.ModelSerializer):
    # sub_name = serializers.CharField(max_length=20)
    # room_number = serializers.IntegerField()
    # url = serializers.CharField(max_length=50)
    class Meta:
        model = Subject
        fields = ('sub_id', 'sub_name', 'room_number', 'url', 'teacher')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course_id', 'course_level', 'course_name', 'url', 'f_id')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('u_id')
