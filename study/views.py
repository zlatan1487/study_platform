from django.shortcuts import render
from rest_framework import viewsets
from study.serliazers import CourseSerializer
from study.models import Course


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    
