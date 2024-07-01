from rest_framework import serializers

from .models import Courses, Teachers, Students


class CoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = '__all__'


class TeachersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teachers
        fields = '__all__'


class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = '__all__'
