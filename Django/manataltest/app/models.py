from django.db import models
import uuid

# Construct school entities
class School(models.Model):
    schoolName = models.CharField(max_length=20)
    schoolAddress = models.CharField(max_length=255)
    maxStudent = models.PositiveIntegerField(null= False)

    def __str__(self):
        return self.schoolName

# Construct student entities
class Student(models.Model):

    # Create method used to randomly select uuid with 20 characters
    def create_id():
        return uuid.uuid1().hex[:20]

    studentId = models.CharField(max_length=20, blank=True, primary_key=True, unique=True, default=create_id)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=80, unique=True)
    gender = models.CharField(max_length=1, null=True)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    schoolId = models.ForeignKey(School, related_name='schoolIds', on_delete=models.CASCADE)

    def __str__(self):
        return self.studentId

   

