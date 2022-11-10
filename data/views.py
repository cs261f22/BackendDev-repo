from django.http import HttpResponse
from django.shortcuts import render
from data.serializers import DepartmentSerializer, MajorSerializer, MinorSerializer
from data.serializers import StudentSerializer, ProfessorSerializer, AdminAssistantSerializer
from data.serializers import CourseSerializer, HighImpactExperienceSerializer, EventSerializer
from data.models import Department, Major, Minor, Student, Professor, AdminAssistant, Course, HighImpactExperience, Event
from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

def api(request):
    return HttpResponse("API Home Page")


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.AllowAny]


class MajorViewSet(viewsets.ViewSet):

    def create(self, request):
        queryset = Major.objects.all()
        serializer = MajorSerializer(queryset, many=True)
        return Response(serializer.data)

    
    def update(self, request, pk=None):
        queryset = Major.objects.all()
        major = get_object_or_404(queryset, pk=pk)
        serializer = MajorSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, pk=None):
         queryset = Major.objects.all()
         major = get_object_or_404(queryset, pk=pk)
         major.delete()

    
    def list(self, request):
        queryset = Major.objects.all()
        serializer = MajorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Major.objects.all()
        major = get_object_or_404(queryset, pk=pk)
        serializer = MajorSerializer(major)
        return Response(serializer.data)

    permission_classes = [permissions.AllowAny]


class MinorViewSet(viewsets.ModelViewSet):
    
    def create(self, request):
        queryset = Minor.objects.all()
        serializer = MinorSerializer(queryset, many=True)
        return Response(serializer.data)

    
    def update(self, request, pk=None):
        queryset = Minor.objects.all()
        minor = get_object_or_404(queryset, pk=pk)
        serializer = MinorSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, pk=None):
         queryset = Minor.objects.all()
         minor = get_object_or_404(queryset, pk=pk)
         minor.delete()

    
    def list(self, request):
        queryset = Minor.objects.all()
        serializer = MinorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Minor.objects.all()
        minor = get_object_or_404(queryset, pk=pk)
        serializer = MinorSerializer(minor)
        return Response(serializer.data)

    permission_classes = [permissions.AllowAny]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class AdminAssistantViewSet(viewsets.ModelViewSet):
    queryset = AdminAssistant.objects.all()
    serializer_class = AdminAssistantSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class HighImpactExperienceViewSet(viewsets.ModelViewSet):
    queryset = HighImpactExperience.objects.all()
    serializer_class = HighImpactExperienceSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.DjangoModelPermissions] 