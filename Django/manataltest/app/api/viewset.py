from django.shortcuts import get_object_or_404
from .serializer import SchoolSerializer, StudentSerializer
from app.models import School, Student
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.exceptions import NotAcceptable

# Construct School view set
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    
# Construct Student view set
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Configure method post action
    def create(self, request):
        schoolId = request.data['schoolId']
        # Retrieve school capacity
        schoolObj = get_object_or_404(School, id=schoolId)
        maxStudent = schoolObj.maxStudent
        studentCount = Student.objects.filter(schoolId=schoolId).count()
        # Only schools which have avilable seat can accept new student
        if studentCount < maxStudent: 
            newStudent = Student(firstName = request.data['firstName'], 
                                 lastName = request.data['lastName'], 
                                 email = request.data['email'],
                                 gender = request.data['gender'],
                                 dob = request.data['dob'],
                                 schoolId = School.objects.get(id = request.data['schoolId']))
            newStudent.save()
            return Response("Student added")
        else: raise NotAcceptable

# Construct StudentInSchool view set
class StudentInSchool(viewsets.ViewSet):
    
    # Configure method post action
    def create(self, request, school_pk=None):
        schoolId = school_pk
        # Retrieve school capacity
        schoolObj = get_object_or_404(School, id=schoolId)
        maxStudent = schoolObj.maxStudent
        studentCount = Student.objects.filter(schoolId=schoolId).count()
        # Only schools which have avilable seat can accept new student
        if studentCount < maxStudent: 
            newStudent = Student(firstName = request.data['firstName'], 
                                 lastName = request.data['lastName'], 
                                 email = request.data['email'],
                                 gender = request.data['gender'],
                                 dob = request.data['dob'],
                                 schoolId = School.objects.get(id = schoolId))
            newStudent.save()
            return Response("Student added")
        else: raise NotAcceptable

    # Configure method get action
    def list(self, request, school_pk=None):
        schoolId = school_pk
        studentsObj = Student.objects.filter(schoolId = schoolId)
        serializer = StudentSerializer(studentsObj, many=True)
        return JsonResponse(serializer.data, safe=False)