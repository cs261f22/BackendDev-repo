from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from data.serializers import DepartmentSerializer, MajorSerializer, MinorSerializer
from data.serializers import StudentSerializer, ProfessorSerializer, AdminAssistantSerializer
from data.serializers import CourseSerializer, HighImpactExperienceSerializer, EventSerializer
from data.models import Department, Major, Minor, Student, Professor, AdminAssistant, Course, HighImpactExperience, \
    Event
from rest_framework import viewsets, permissions

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request


def api(request):
    return HttpResponse("API Home Page")


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = Department.objects.all()
        serializer_class = DepartmentSerializer
        permission_classes = [permissions.AllowAny]
        return HttpResponse(serializer_class.data)

    def retrieve(self, request, pk=None):
        queryset = Department.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer_class = DepartmentSerializer
        permission_classes = [permissions.AllowAny]
        return HttpResponse(serializer_class.data)


class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    permission_classes = [permissions.AllowAny]

    @action(methods=["DELETE"], detail=False, permission_classes=[permissions.AllowAny])
    def delete(self, request: Request):
        queryset = Major.objects.all()
        delete_id = request.data
        delete_albums = self.queryset.filter(id__in=delete_id)
        delete_albums.delete()
        return Response(self.serializer_class(delete_albums, many=True).data)

    def list(self, request):
        queryset = Major.objects.all()
        serializer_class = MajorSerializer
        permission_classes = [permissions.AllowAny]
        return HttpResponse(serializer_class.data)

    def retrieve(self, request, pk=None):
        queryset = Major.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer_class = MajorSerializer
        permission_classes = [permissions.AllowAny]
        return HttpResponse(serializer_class.data)

    def update(self, request, *args, **kwargs):

        queryset = Major.objects.all()
        serializer_class = MajorSerializer
        permission_classes = [permissions.AllowAny]

        instance = self.get_object()
        instance.major = request.data.get("Major")
        instance.save()
        self.perform_update(serializer_class)

        return HttpResponse(serializer_class.data)

class MinorViewSet(viewsets.ModelViewSet):
    queryset = Minor.objects.all()
    serializer_class = MinorSerializer
    permission_classes = [permissions.DjangoModelPermissions]


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
