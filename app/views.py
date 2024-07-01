from django.shortcuts import render

from .models import Courses, Teachers, Students

from .serializers import CoursesSerializer, TeachersSerializer, StudentsSerializer

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly



class CoursesRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]



class TeachersRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class StudentsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    

