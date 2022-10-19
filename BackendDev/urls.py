"""BackendDev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from BackendDev import views as main_views
from data import views as data_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'HighImpactExperiences', data_views.HighImpactExperiencesViewSet) #access: localhost:8000/api/HighImpactExperiences
router.register(r'Departments', data_views.DepartmentsViewSet) #access: localhost:8000/api/Departments
router.register(r'Faculty', data_views.FacultyViewSet) #access: localhost:8000/api/Faculty
router.register(r'Courses', data_views.CoursesViewSet) #access: localhost:8000/api/Courses
router.register(r'Majors', data_views.MajorsViewSet) #access: localhost:8000/api/Majors
router.register(r'Minors', data_views.MinorsViewSet) #access: localhost:8000/api/Minors
router.register(r'Students', data_views.StudentsViewSet) #access: localhost:8000/api/Students
router.register(r'Events', data_views.EventsViewSet) #access: localhost:8000/api/Events

urlpatterns = [
    path('admin/', admin.site.urls), #access: localhost:8000/admin/
    path('', main_views.index, name='index'), #access: localhost:8000/
    path('files/', main_views.files, name='files'), #access: localhost:8000/files/
    #path('api/', data_views.api, name='api'), #access: localhost:8000/api/
    path('api/', include(router.urls)) #access: localhost:8000/api/[router.url]
]
