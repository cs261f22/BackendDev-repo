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


class DepartmentViewSet(viewsets.ViewSet):
    
    def create(self, request):
        queryset = Department.objects.all()
        serializer = DepartmentSerializer(queryset, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
    def update(self, request, pk=None):
        queryset = Department.objects.all()
        department = get_object_or_404(queryset, pk=pk)
        serializer = DepartmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, pk=None):
         queryset = Department.objects.all()
         department = get_object_or_404(queryset, pk=pk)
         department.delete()

    
    def list(self, request):
        queryset = Department.objects.all()
        serializer = DepartmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Department.objects.all()
        department = get_object_or_404(queryset, pk=pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    permission_classes = [permissions.AllowAny]


class MajorViewSet(viewsets.ViewSet):

    def create(self, request):
        queryset = Major.objects.all()
        serializer = MajorSerializer(queryset, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
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


class MinorViewSet(viewsets.ViewSet):
    
    def create(self, request):
        queryset = Minor.objects.all()
        serializer = MinorSerializer(queryset, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
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


class StudentViewSet(viewsets.ViewSet):
    
    def create(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
    def update(self, request, pk=None):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, pk=None):
         queryset = Student.objects.all()
         student = get_object_or_404(queryset, pk=pk)
         student.delete()

    
    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    permission_classes = [permissions.AllowAny]


class ProfessorViewSet(viewsets.ViewSet):
    
    def create(self, request):
        queryset = Professor.objects.all()
        serializer = ProfessorSerializer(queryset, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
    def update(self, request, pk=None):
        queryset = Professor.objects.all()
        professor = get_object_or_404(queryset, pk=pk)
        serializer = ProfessorSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, pk=None):
         queryset = Professor.objects.all()
         professor = get_object_or_404(queryset, pk=pk)
         professor.delete()

    
    def list(self, request):
        queryset = Professor.objects.all()
        serializer = ProfessorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Professor.objects.all()
        professor = get_object_or_404(queryset, pk=pk)
        serializer = ProfessorSerializer(professor)
        return Response(serializer.data)

    permission_classes = [permissions.AllowAny]


class AdminAssistantViewSet(viewsets.ViewSet):
    
    def create(self, request):
        queryset = AdminAssistant.objects.all()
        serializer = AdminAssistantSerializer(queryset, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
    def update(self, request, pk=None):
        queryset = AdminAssistant.objects.all()
        adminassistant = get_object_or_404(queryset, pk=pk)
        serializer = AdminAssistantSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, pk=None):
         queryset = AdminAssistant.objects.all()
         adminassistant = get_object_or_404(queryset, pk=pk)
         adminassistant.delete()

    
    def list(self, request):
        queryset = AdminAssistant.objects.all()
        serializer = AdminAssistantSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = AdminAssistant.objects.all()
        adminassistant = get_object_or_404(queryset, pk=pk)
        serializer = AdminAssistantSerializer(adminassistant)
        return Response(serializer.data)

    permission_classes = [permissions.AllowAny]


class CourseViewSet(viewsets.ViewSet):
    
    def create(self, request):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
    def update(self, request, pk=None):
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, pk=None):
         queryset = Course.objects.all()
         course = get_object_or_404(queryset, pk=pk)
         course.delete()

    
    def list(self, request):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    permission_classes = [permissions.AllowAny]


class HighImpactExperienceViewSet(viewsets.ViewSet):
    
    def create(self, request):
        queryset = HighImpactExperience.objects.all()
        serializer = HighImpactExperienceSerializer(queryset, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
    def update(self, request, pk=None):
        queryset = HighImpactExperience.objects.all()
        highImpactExperience = get_object_or_404(queryset, pk=pk)
        serializer = HighImpactExperienceSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, pk=None):
         queryset = HighImpactExperience.objects.all()
         highImpactExperience = get_object_or_404(queryset, pk=pk)
         highImpactExperience.delete()

    
    def list(self, request):
        queryset = HighImpactExperience.objects.all()
        serializer = HighImpactExperienceSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = HighImpactExperience.objects.all()
        highImpactExperience = get_object_or_404(queryset, pk=pk)
        serializer = HighImpactExperienceSerializer(highImpactExperience)
        return Response(serializer.data)

    permission_classes = [permissions.AllowAny]


class EventViewSet(viewsets.ViewSet):
    
    def create(self, request):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
    def update(self, request, pk=None):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=pk)
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, pk=None):
         queryset = Event.objects.all()
         event = get_object_or_404(queryset, pk=pk)
         event.delete()

    
    def list(self, request):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    permission_classes = [permissions.AllowAny] 