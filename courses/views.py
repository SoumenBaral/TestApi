from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer

def home(request):
    return HttpResponse('Welcome To Our Courses Api Server')

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
