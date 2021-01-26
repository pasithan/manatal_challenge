from rest_framework import serializers
from app.models import School, Student

# Construct serializer for School model
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'schoolName', 'schoolAddress', 'maxStudent']

# Construct serializer for Student model
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['studentId', 'firstName', 'lastName', 'email', 'gender', 'dob', 'schoolId']
